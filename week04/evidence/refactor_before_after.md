# W4 重构前后对比

## 重构前
- 文件：week02/unit_converter.py
- 结构：顺序执行（输入、计算、输出全部混在一起）
- 问题：
  1. 换算公式直接写在主程序里，无法被其他程序复用；
  2. 每次想单独测试一个换算，必须把整个程序跑一遍；
  3. 如果公式要修改，需要找到对应位置修改，容易改漏；
  4. 输入、计算、输出职责未分离，代码越长越难维护。

## 重构后
- 文件：week04/converters.py（纯计算模块）
- 文件：week04/unit_converter_func.py（主程序）
- 结构：
  1. 计算逻辑全部在 converters.py 中；
  2. 主程序只负责输入和输出；
  3. 通过 `import converters` 调用模块。
- 改进：
  1. **可复用**：其他程序可以直接 import converters 使用换算函数；
  2. **可测试**：可以单独测试 `celsius_to_fahrenheit(100)` 返回 `212.0`；
  3. **可维护**：公式修改只需改 converters.py 一处；
  4. **职责分离**：主程序管交互，模块管计算；
  5. **可审计**：旧文件保留，Git 有完整提交记录。

## 证据
- 原文件（未修改）：week02/unit_converter.py
- 新模块：week04/converters.py
- 新主程序：week04/unit_converter_func.py
- 手动测试输出：week04/evidence/terminal_output_w4.txt
- Git commit：（稍后填写）