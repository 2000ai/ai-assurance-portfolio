# W8 学习日志

日期：2026-10-14
学习时长：约 4 小时
学习内容：
- 申请智谱 API Key，理解 HTTP 调用本质
- .env + python-dotenv 管理密钥
- 用 OpenAI SDK 和 requests 两种方式调用 API
- messages 结构：system/user/assistant
- 多轮对话与上下文丢失实验
- 封装 LLMClient，异常处理与日志
- 命令行机器人 chatbot.py + 脱敏留痕
- 报错定位训练：401/404/429

产出物：
- week07/ai_assurance_tools/llm_client.py
- week08/chatbot.py
- week08/practice/api_hello_w8.py
- week08/practice/api_hello_requests_w8.py
- week08/practice/messages_practice_w8.py
- week08/practice/no_context_w8.py
- week08/practice/error_repro_test_w8.py
- week08/evidence/api_call_notes_w8.md
- week08/evidence/context_loss_finding_w8.md
- week08/evidence/error_repro_w8.md
- week08/evidence/api_trace_w8.log（脱敏）
- week08/evidence/api_trace_raw_w8.log（原始，不提交）

关键命令：
- python week08/practice/api_hello_w8.py
- python week08/chatbot.py
- python week08/practice/error_repro_test_w8.py

踩坑记录：
- 坑：多轮对话不带历史导致模型“脑补”指代。
- 报错原文：无报错，属于逻辑错误。
- 解决：记录为上下文丢失发现，写进 context_loss_finding_w8.md。

四栏小结：
- 见 four_column_summary_w8.md

独立性自问：
- 见 independence_self_check_w8.md

下周计划：
- 进入阶段 1，学习 AI 审计准则与证据规则。