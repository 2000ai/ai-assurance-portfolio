# W7 四栏小结

## 发现
- 完成 FileOrganizer 类封装，比 W6 函数式版本更易复用。
- 完成 venv + pip + pyproject.toml 打包。
- 在干净 venv 中按 README 安装并运行成功。
- 发现依赖未固定版本时，环境不可复现。

## 证据
- 包目录：week07/ai_assurance_tools/
- 入口脚本：week07/run_organizer.py
- 打包配置：week07/pyproject.toml
- 依赖记录：week07/requirements.txt
- 干净环境测试：week07/evidence/clean_env_test_w7.md
- 依赖清单：week07/evidence/dependency_manifest_w7.md
- 终端输出：week07/evidence/terminal_output_w7.txt
- Git commit：（提交后补充）

## 风险
- requirements.txt 未固定所有间接依赖版本。
- README 未覆盖所有操作系统（Windows 激活命令未实测）。
- 包名与模块名可能冲突（连字符 vs 下划线），需统一。
- 错误日志可能含敏感路径。
- 未加自动化测试，仅手动测试。
- 版本号未遵循语义化版本。

## 建议
- W8 前补 pytest 基础测试。
- 固定依赖版本，保证可复现。
- 加 LICENSE、CHANGELOG。
- 后续用 GitHub Actions 做安装测试。
- 错误日志提交前脱敏。