# W8 Day5: 消息结构与多轮对话练习
from dotenv import load_dotenv
load_dotenv()

from ai_assurance_tools import LLMClient

client = LLMClient(error_log="week08/evidence/error_log_w8.log")

# 初始化 messages，只放一条 system
messages = [
    {"role": "system", "content": "你是一个简洁的审计助手，回答不超过两句话。"},
]

print("=== 多轮对话练习 ===")
print("输入 quit 或 exit 退出。\n")

while True:
    user_input = input("你: ").strip()

    if user_input.lower() in ("quit", "exit"):
        print("对话结束。")
        break

    if not user_input:
        continue

    # 1. 把用户输入加入 messages
    messages.append({"role": "user", "content": user_input})

    # 2. 发送请求
    result = client.chat(messages)

    if result["ok"]:
        reply = result["content"]
        print(f"助手: {reply}")

        # 3. 把模型回复也加入 messages（保持上下文）
        messages.append({"role": "assistant", "content": reply})

        # 4. 打印当前 messages 长度和 token 消耗
        print(f"  [当前消息数: {len(messages)}, 本轮 token: {result['usage'].total_tokens if result['usage'] else 'N/A'}]")
    else:
        print(f"错误: {result['error']}")
        # 如果失败，把刚才加的 user 消息移除，避免污染历史
        messages.pop()