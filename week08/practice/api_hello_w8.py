# W8 Day3: 最小 API 调用（方式 A：OpenAI SDK）
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件中的环境变量
load_dotenv()

# 2. 创建客户端
client = OpenAI(
    api_key=os.getenv("ZAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

# 3. 发起请求
response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "你是一个简洁的审计助手，回答不超过三句话。"},
        {"role": "user", "content": "用一句话解释什么是审计证据。"},
    ],
    stream=False,
)

# 4. 提取回答
print(response.choices[0].message.content)

# 5. 打印 token 消耗（审计证据的一部分）
print("\n--- Token 消耗 ---")
print("输入 tokens:", response.usage.prompt_tokens)
print("输出 tokens:", response.usage.completion_tokens)
print("总计 tokens:", response.usage.total_tokens)