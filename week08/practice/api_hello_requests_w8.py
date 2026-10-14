# W8 Day3: 最小 API 调用（方式 B：requests 裸发，理解 HTTP 本质）
import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('ZAI_API_KEY')}",
    "Content-Type": "application/json",
}

data = {
    "model": "glm-4-flash",
    "messages": [
        {"role": "user", "content": "用一句话解释什么是审计证据。"}
    ],
}

resp = requests.post(url, headers=headers, json=data, timeout=30)

print("HTTP 状态码:", resp.status_code)
print("响应体:")
print(resp.json())