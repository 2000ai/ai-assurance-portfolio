# W1 学习日志 v1

日期：2026-10-08
学习时长：约 2 小时
学习内容：
- 环境搭建（Miniconda, VS Code, Git, GitHub Desktop）
- 运行 Python 脚本并保存输出
- 使用 Git 进行本地版本控制和 GitHub 远程推送

产出物：
- hello_audit.py
- env_check.py
- GitHub 仓库 ai-assurance-portfolio

关键命令：
- conda create -n ai-assurance python=3.12 -y
- python week01/hello_audit.py > week01/evidence/terminal_output_w1.txt
- git add . && git commit -m "..."

踩坑记录：
- 坑：conda 创建环境时提示 Terms of Service 未接受
- 报错原文：CondaToSNonInteractiveError: Terms of Service have not been accepted...
- 解决：运行 conda tos accept 命令接受条款
- 参考：终端报错提示

四栏小结：
- 发现：环境可以创建，脚本可以运行。
- 证据：week01/evidence/terminal_output_w1.txt
- 风险：目前还无法独立解决依赖冲突。
- 建议：下周学习变量与输入输出，继续保留原始输出。

下周计划：完成第3-4章学习，写一个简单的审计计算脚本。