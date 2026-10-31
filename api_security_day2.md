## 三、实战 3：IDOR 越权下载敏感文件
- **靶场**：PortSwigger - Insecure direct object references (IDOR)
- **攻击手法**：
  1. 找到“Live chat”中的“View transcript”功能，抓取 `GET /download-transcript/1.txt` 请求。
  2. 在 Burp Repeater 中，将文件名修改为 `2.txt`。
  3. 遍历后成功下载到目标用户 `carlos` 的聊天记录。
  4. 从聊天记录中提取出 `carlos` 的明文密码 `hw0xg3evsq09ag356apm`。
  5. 退出当前账号，使用 `carlos` 和该密码成功登录，接管账户。
- **风险**：极其严重的敏感数据泄露与越权，攻击者可利用此漏洞批量窃取用户隐私，或接管高权限账户。
- **证据留存**：[插入你抓到密码的截图 + 登录 carlos 成功的截图]

## 五、关联《AI-Red 指南》
- API 越权（BOLA/IDOR）是 AI 系统最常面临的风险之一。
- 如果 AI Agent 的会话记忆（Memory）或 RAG 检索接口没有做严格的权限校验，攻击者只需修改 ID 就能窃取他人的对话或内部知识库。