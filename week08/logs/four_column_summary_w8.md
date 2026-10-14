# W8 四栏小结

## 发现
- 完成命令行问答机器人 v1，支持多轮对话。
- 密钥通过 .env + python-dotenv 管理，未硬编码，未入库。
- 请求/响应已脱敏留痕，原始日志本地保留。
- 发现多轮对话会持续增加 messages 长度，token 消耗递增。
- 发现不带历史时模型会“脑补”指代，导致回答偏离原意。
- 发现 401/404/429 等 API 错误可通过状态码和 traceback 定位。

## 证据
- 机器人：week08/chatbot.py
- 封装：week07/ai_assurance_tools/llm_client.py
- 脱敏日志：week08/evidence/api_trace_w8.log
- 原始日志（不提交）：week08/evidence/api_trace_raw_w8.log
- 报错训练：week08/evidence/error_repro_w8.md
- 上下文丢失发现：week08/evidence/context_loss_finding_w8.md
- 终端输出：week08/evidence/terminal_output_w8.txt
- Git commit：

## 风险
- .env 若误提交，密钥会泄露；已确认 .gitignore 覆盖。
- 多轮对话无 token 上限控制，可能超预算。
- 无重试机制，网络抖动会直接失败。
- 脱敏规则只覆盖 API Key，未覆盖 PII。
- 无流式输出，长回复体验差。
- 错误日志可能含请求体，需持续脱敏检查。

## 建议
- 加 token 计数与预算上限。
- 加指数退避重试（参考 openai SDK 内置重试）。
- 扩展脱敏规则：手机号、邮箱、身份证。
- 后续加流式输出。
- 把 API 调用封装进 W7 可安装包，发布新版本。