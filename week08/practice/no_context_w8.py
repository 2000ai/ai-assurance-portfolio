# W8 Day5: 对比实验——不传历史会怎样？
from dotenv import load_dotenv
load_dotenv()

from ai_assurance_tools import LLMClient

client = LLMClient(error_log="week08/evidence/error_log_w8.log")

# 第 1 轮
messages1 = [
    {"role": "system", "content": "你是一个简洁的审计助手。"},
    {"role": "user", "content": "什么是工作底稿？"},
]
result1 = client.chat(messages1)
print("第 1 轮回答:", result1["content"])

# 第 2 轮：故意不带历史
messages2 = [
    {"role": "system", "content": "你是一个简洁的审计助手。"},
    {"role": "user", "content": "它和普通笔记有什么区别？"},
]
result2 = client.chat(messages2)
print("第 2 轮回答（不带历史）:", result2["content"])