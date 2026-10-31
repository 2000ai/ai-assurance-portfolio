import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import subprocess

# ☠️ 模拟开发者的致命错误：把机密存在环境变量里
os.environ["CLOUD_ACCESS_KEY"] = "AKIAIOSFODNN7EXAMPLE"
os.environ["AI_MODEL_API_KEY"] = "sk-ZhiPu-Secret-Key-2026"

class VulnerableHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/process_image":
            # 获取用户传入的图片名称
            query = urllib.parse.parse_qs(parsed_path.query)
            image_name = query.get("name", [""])[0]
            
            # ☠️ 致命漏洞：直接把用户输入拼接到系统命令中
            # 模拟 AI 系统调用外部工具处理图片
            cmd = f"echo 'Processing image: {image_name}'"
            
            try:
                # 执行命令
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                self.send_response(200)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(f"AI 助手回复：处理成功\n{result}".encode())
            except subprocess.CalledProcessError as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(e.output.encode())

if __name__ == "__main__":
    print("🚀 AI 图像处理微服务已启动，监听端口 8081...")
    print("⚠️ 请在另一个终端窗口进行攻击测试。")
    HTTPServer(("0.0.0.0", 8081), VulnerableHandler).serve_forever()