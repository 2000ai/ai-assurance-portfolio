# W8 API 调用笔记

## 一、服务商信息
- 服务商名称：DeepSeek
- 注册地址：https://platform.deepseek.com
- API Key 申请地址：https://platform.deepseek.com/api_keys
- 计费方式：按 token 计费，充了 [X] 元
- 密钥存储位置（Day1 临时）：[备忘录，尚未放入 .env]

## 二、Base URL 与模型
- Base URL：https://api.deepseek.com
- 模型名：deepseek-chat
- 端点：/chat/completions

## 三、一次 API 调用的组成

### 请求（Request）
- HTTP 方法：POST
- 端点路径：/chat/completions
- 请求头：
  - Authorization: Bearer sk-***
  - Content-Type: application/json
- 请求体字段：
  - model：指定使用的模型
  - messages：对话内容数组
  - stream：是否流式输出（false 表示一次性返回）

### 响应（Response）
- HTTP 状态码：
  - 200：成功
  - 401：密钥错误
  - 404：地址错误
  - 429：请求太频繁
- 响应体关键字段：
  - choices[0].message.content：模型的回答
  - usage.prompt_tokens：输入消耗的 token
  - usage.completion_tokens：输出消耗的 token
  - usage.total_tokens：总消耗

## 四、messages 结构
messages 是一个数组，每个元素包含 role 和 content：
- role: system —— 设定模型行为（相当于“人设”）
- role: user —— 用户输入（你的问题）
- role: assistant —— 模型的回复（历史对话）

## 五、密钥管理
- 存储位置：.env（Day2 创建）
- 是否硬编码：否
- 是否入库：否
- 是否截图/聊天工具传播：否

## 六、安全原则
1. 密钥不入库、不硬编码、不截图、不贴聊天记录。
2. 密钥用环境变量管理，代码从 os.getenv() 读取。
3. 请求/响应留痕时脱敏（密钥替换为 sk-***）。
4. 原始日志本地保留，脱敏日志才提交。