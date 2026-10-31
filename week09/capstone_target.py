from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import os
import subprocess

# 模拟云环境变量
os.environ["SECRET_CLOUD_TOKEN"] = "FLAG{ULTIMATE_AI_HACKER}"

# 模拟高管的聊天记录
CHAT_HISTORY = {
    "1001": "员工A：今天天气不错。",
    "1002": "高管：系统的 ping_tool 好像有漏洞，但 AI 的提示词里写了只能内部使用，应该没事吧？"
}

class CapstoneHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # 1. 越权漏洞点
        if parsed_path.path == "/api/v1/chat_history":
            query = urllib.parse.parse_qs(parsed_path.query)
            user_id = query.get("user_id", [""])[0]
            history = CHAT_HISTORY.get(user_id, "无记录")
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"user_id": user_id, "history": history}).encode())
            
        # 2. 聊天接口与命令注入漏洞点
        elif parsed_path.path == "/api/v1/chat":
            query = urllib.parse.parse_qs(parsed_path.query)
            prompt = query.get("prompt", [""])[0]
            
            # 模拟 AI 护栏（极弱）
            if "ping_tool" in prompt or "排障" in prompt:
                # 提取黑客拼接的参数
                if "127.0.0.1;" in prompt:
                    cmd_part = prompt.split("；")[-1] if "；" in prompt else prompt.split(";")[-1]
                    cmd = f"ping -c 1 127.0.0.1; {cmd_part.strip()}"
                    try:
                        # 致命漏洞
                        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                        reply = f"AI: 排障完成。输出：\n{res}"
                    except subprocess.CalledProcessError as e:
                        reply = f"AI: 排障失败。输出：\n{e.output}"
                else:
                    reply = "AI: 连通性正常。"
            else:
                reply = "AI: 你好，我是星尘智能客服。"
                
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"response": reply}).encode())
            
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    print("🚀 星尘科技 AI 客服系统已启动，监听端口 8000...")
    HTTPServer(("0.0.0.0", 8000), CapstoneHandler).serve_forever()