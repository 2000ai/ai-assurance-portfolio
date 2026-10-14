# W7 学习日志

日期：2026-10-14
学习时长：约 4 小时
学习内容：
- 类与对象：class、__init__、self、属性、方法
- 封装与方法拆分：私有属性、__str__
- venv 创建与激活
- pip install、pip freeze
- pyproject.toml 打包配置
- 可编辑安装 pip install -e .
- 干净环境复现测试

产出物：
- practice/class_basics.py
- practice/encapsulation_practice.py
- ai_assurance_tools/__init__.py
- ai_assurance_tools/logging_utils.py
- ai_assurance_tools/organizer.py
- run_organizer.py
- pyproject.toml
- README.md
- requirements.txt
- clean_env_test_w7.md
- dependency_manifest_w7.md

关键命令：
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -e .
- pip freeze > requirements.txt
- python run_organizer.py
- git add . && git commit -m "..." && git push

踩坑记录：
- 坑：在 conda 环境里建 venv，解释器路径混乱。
- 报错原文：ModuleNotFoundError: No module named 'ai_assurance_tools'
- 行号：不适用
- 解决：先 conda deactivate，再用 python3 -m venv .venv 重建。
- 参考：Python 官方 venv 文档。

四栏小结：
- 见 four_column_summary_w7.md

独立性自问：
- 见 independence_self_check_w7.md

下周计划：
- 学习大模型 API 调用。
- 把包扩展为带 LLM 客户端的安全工具。
- 加环境变量管理密钥，不入库。