# W8 Day7: 报错定位训练
from dotenv import load_dotenv
load_dotenv()

from ai_assurance_tools import LLMClient

# 正常调用（对照组）
print("=== 正常调用 ===")
client_ok = LLMClient(error_log="week08/evidence/error_log_w8.log")
result = client_ok.chat([{"role": "user", "content": "你好"}])
print("ok:", result["ok"])
print("content:", result["content"])
print()

# 错误 1：401 错误密钥
print("=== 错误 1：401 错误密钥 ===")
client_401 = LLMClient(
    api_key="sk-invalid-key-for-testing",
    error_log="week08/evidence/error_log_w8.log"
)
result_401 = client_401.chat([{"role": "user", "content": "你好"}])
print("ok:", result_401["ok"])
print("error:", result_401["error"])
print()

# 错误 2：404 错误 base_url
print("=== 错误 2：404 错误 base_url ===")
client_404 = LLMClient(
    base_url="https://open.bigmodel.cn/api/paas/v4/wrongpath",
    error_log="week08/evidence/error_log_w8.log"
)
result_404 = client_404.chat([{"role": "user", "content": "你好"}])
print("ok:", result_404["ok"])
print("error:", result_404["error"])

# W8 Day7: 尝试触发 429
import time
from dotenv import load_dotenv
load_dotenv()

from ai_assurance_tools import LLMClient

client = LLMClient(error_log="week08/evidence/error_log_w8.log")

# 错误 3：400 messages 结构错误
print("=== 错误 3：400 messages 结构错误 ===")
client_400 = LLMClient(error_log="week08/evidence/error_log_w8.log")
result_400 = client_400.chat("这不是一个数组")  # 故意传错类型
print("ok:", result_400["ok"])
print("error:", result_400["error"])