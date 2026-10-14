# W7 错误记录笔记

## 错误 1：ModuleNotFoundError
- 触发场景：未 pip install -e .，直接运行 run_organizer.py
- 错误原文：ModuleNotFoundError: No module named 'ai_assurance_tools'
- 处理方法：在 week07/ 目录执行 pip install -e .

## 错误 2：包名与目录名冲突
- 触发场景：pyproject.toml 的 name 写成 "ai_assurance_tools"（下划线）
- 现象：pip 能装，但 import 路径混乱
- 处理方法：name 用连字符 "ai-assurance-tools"，目录名用下划线 "ai_assurance_tools"

## 错误 3：__init__.py 缺失
- 触发场景：ai_assurance_tools/ 目录没有 __init__.py
- 现象：pip 装完 import 报错
- 处理方法：新建 __init__.py，声明 __all__ 和 __version__

## 错误 4：venv 与 conda 混合
- 触发场景：conda 环境下激活 venv
- 现象：which python 指向 conda 路径
- 处理方法：先 conda deactivate 再 source .venv/bin/activate

## 错误 5：依赖未固定版本
- 触发场景：requirements.txt 只写包名不写版本
- 现象：别人装的环境和你不一致，结果不可复现
- 处理方法：pip freeze > requirements.txt