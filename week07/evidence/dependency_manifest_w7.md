# W7 依赖清单

## Python
- 版本：3.12.x
- 解释器路径：/opt/homebrew/bin/python3（创建 venv 时使用）

## 虚拟环境
- 路径：week07/.venv
- 创建命令：python3 -m venv .venv

## 直接依赖
- 无第三方依赖（仅标准库：os、shutil、traceback、datetime）

## 开发依赖
- 无

## 打包工具
- setuptools >= 68
- wheel

## 依赖记录方式
- pyproject.toml（声明打包与元数据）
- requirements.txt（pip freeze 生成，用于复现第三方依赖）

## 复现命令
```bash
cd week07
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python run_organizer.py