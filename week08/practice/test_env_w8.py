import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

api_key = os.getenv("ZAI_API_KEY")
base_url = os.getenv("ZAI_BASE_URL")
model = os.getenv("ZAI_MODEL")

print("API Key 是否加载:", "是" if api_key else "否")
print("API Key 前 8 位:", api_key[:8] + "***" if api_key else "未设置")
print("Base URL:", base_url)
print("模型:", model)