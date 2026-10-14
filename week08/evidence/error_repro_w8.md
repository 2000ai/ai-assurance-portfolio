# W8 报错定位训练

## 报错 1：401 Unauthorized
- 现象：AuthenticationError: Error code: 401
- 定位：`llm_client.py` 第 X 行，`client.chat.completions.create`
- 原因：API Key 错误或未加载
- 查文档：智谱文档确认 Authorization 头格式为 `Bearer <API_KEY>`
- 修复：检查 `.env` 中 `ZAI_API_KEY` 是否正确，`load_dotenv()` 是否在 `LLMClient()` 创建前调用
- 证据：`error_log_w8.log` 中 `AuthenticationError` 记录

## 报错 2：404 Not Found
- 现象：NotFoundError: Error code: 404
- 定位：`llm_client.py` 中 `base_url` 配置错误
- 原因：`base_url` 写成了 `https://open.bigmodel.cn/api/paas/v4/wrongpath`
- 查文档：智谱文档要求 `base_url = "https://open.bigmodel.cn/api/paas/v4/"`
- 修复：改为正确 `base_url`
- 证据：`error_log_w8.log` 中 `NotFoundError` 记录

## 报错 3：429 Rate Limit（或 400 BadRequest）
- 现象：[填写你实际观察到的]
- 定位：[填写]
- 原因：[填写]
- 查文档：[填写]
- 修复：[填写]
- 证据：[填写]

## 结论
三种错误均能通过错误类型、traceback 和日志定位，并修复。