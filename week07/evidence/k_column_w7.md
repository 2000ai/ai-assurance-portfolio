# W7 卡壳记录（K 列）

| 日期 | 任务 | 卡壳分钟 | 报错原文/现象 | 已尝试 | 求助对象 | 结果 | 后续 |
|---|---|---|---|---|---|---|---|
| 2026-10-14 | conda 与 venv 冲突 | 15 | 激活 venv 后路径仍指向 conda | 检查 which python | 自己 | 先 conda deactivate 再建 venv | 记住两者不混用 |
| 2026-10-14 | 包导入失败 | 20 | ModuleNotFoundError: No module named 'ai_assurance_tools' | 检查 pyproject.toml | 自己 | pip install -e . 安装后即可 | 记住包必须安装 |
| 2026-10-14 | pyproject.toml 配置 | 10 | 打包找不到包 | 检查 include 字段 | 自己 | 改成 ["ai_assurance_tools*"] | 注意包名与目录名 |