# W4 四栏小结

## 发现
- 完成 W2 单位换算器的函数版重构。
- 发现 W2 的已知局限仍然存在：输入非数字会 ValueError。
- 发现函数版让换算逻辑可以单独调用和测试。

## 证据
- 原脚本：week02/unit_converter.py
- 换算模块：week04/converters.py
- 函数版主程序：week04/unit_converter_func.py
- 终端输出：week04/evidence/terminal_output_w4.txt
- 手动测试结果：
  - converters.celsius_to_fahrenheit(100) -> 212.0
  - converters.kilometers_to_miles(1) -> 0.621371
  - converters.kilograms_to_pounds(1) -> 2.20462
- Git commit：（稍后填写）

## 风险
- 输入非数字仍会崩溃，异常处理留到 W6。
- 尚无自动化单元测试，目前只有手动测试。
- 浮点数精度有限，结果保留两位小数。
- 函数没有完整文档字符串和类型注解。
- 主程序仍是顺序执行，没有菜单和循环。

## 建议
- W5 学列表与字典后，可做批量换算。
- W6 学异常处理后，加 try/except 处理非法输入。
- W7 学虚拟环境和打包后，把 converters 做成可安装小包。
- 后续加 pytest 单元测试，验证边界值。