# W8 Day6: 命令行问答机器人 v1（带脱敏留痕）
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from ai_assurance_tools import LLMClient

# 日志路径
TRACE_LOG = "week08/evidence/api_trace_w8.log"          # 脱敏版，提交
RAW_LOG = "week08/evidence/api_trace_raw_w8.log"        # 原始版，不提交

client = LLMClient(error_log="week08/evidence/error_log_w8.log")

# messages 初始化
messages = [
    {"role": "system", "content": "你是一个简洁的审计助手，回答不超过三句话。"},
]


def mask_sensitive(text):
    """脱敏：把 API Key 和个人信息替换掉"""
    if not text:
        return text
    api_key = os.getenv("ZAI_API_KEY", "")
    if api_key:
        text = text.replace(api_key, "sk-***")
    return text


def write_trace(request_messages, response_content, usage):
    """写请求/响应留痕：脱敏版 + 原始版"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 原始版（本地保留）
    raw_obj = {
        "timestamp": timestamp,
        "request": {"model": client.model, "messages": request_messages},
        "response": {
            "content": response_content,
            "usage": usage.model_dump() if usage else None,
        },
    }

    # 脱敏版（提交 GitHub）
    masked_obj = {
        "timestamp": timestamp,
        "request": {
            "model": client.model,
            "messages": [
                {"role": m["role"], "content": mask_sensitive(m["content"])}
                for m in request_messages
            ],
        },
        "response": {
            "content": mask_sensitive(response_content),
            "usage": raw_obj["response"]["usage"],
        },
    }

    os.makedirs(os.path.dirname(TRACE_LOG), exist_ok=True)

    with open(TRACE_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] MASKED\n")
        f.write(json.dumps(masked_obj, ensure_ascii=False, indent=2))
        f.write("\n" + "-" * 80 + "\n")

    with open(RAW_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] RAW\n")
        f.write(json.dumps(raw_obj, ensure_ascii=False, indent=2))
        f.write("\n" + "-" * 80 + "\n")


def main():
    print("=== 命令行问答机器人 v1 ===")
    print("命令：quit/exit 退出 | clear 清空历史")
    print()

    while True:
        user_input = input("你: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("对话结束。")
            break
        if user_input.lower() == "clear":
            messages[:] = [messages[0]]   # 保留 system，清空历史
            print("已清空对话历史。")
            continue

        # 加入用户输入
        messages.append({"role": "user", "content": user_input})

        # 发送请求
        result = client.chat(messages)

        if result["ok"]:
            reply = result["content"]
            print(f"助手: {reply}")

            # 加入模型回复
            messages.append({"role": "assistant", "content": reply})

            # 写留痕日志
            write_trace(messages, reply, result["usage"])

            # 显示消息数
            print(f"  [消息数: {len(messages)}, 本轮 token: {result['usage'].total_tokens if result['usage'] else 'N/A'}]")
        else:
            print(f"错误: {result['error']}")
            messages.pop()  # 移除刚才加的 user 消息


if __name__ == "__main__":
    main()