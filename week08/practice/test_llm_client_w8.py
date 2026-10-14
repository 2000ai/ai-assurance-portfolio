# W8 Day4: 测试 LLMClient 封装
from pathlib import Path
from dotenv import load_dotenv

# 找到项目根目录的 .env
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from ai_assurance_tools import LLMClient

client = LLMClient(error_log="week08/evidence/error_log_w8.log")

result = client.chat([
    {"role": "system", "content": "你是一个简洁的审计助手，回答不超过两句话。"},
    {"role": "user", "content": "什么是审计证据？"},
])

if result["ok"]:
    print("回答:", result["content"])
    print(f"耗时: {result['elapsed']:.2f} 秒")
    if result["usage"]:
        print(f"Token 消耗: {result['usage'].total_tokens}")
else:
    print("请求失败:", result["error"])