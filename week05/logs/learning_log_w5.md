# W5 学习日志

日期：2026-10-13
学习时长：约 3 小时
学习内容：
- 列表：创建、索引、切片、append、len、in、遍历、sort
- 字典：增删改查、get、keys/values/items
- 字符串：lower、strip、replace、split
- 词频统计思路与实现

产出物：
- practice/list_practice.py
- practice/dict_practice.py
- practice/string_practice.py
- word_freq_v0.py
- word_freq.py
- counting_criteria_w5.md
- evidence_chain_w5.md

关键命令：
- python week05/word_freq.py
- git add . && git commit -m "..." && git push

踩坑记录：
- 坑：v0 版本标点未清洗，great. 和 great 被当成两个词。
- 报错原文：无报错，属于逻辑错误（统计口径问题）。
- 行号：不适用。
- 解决：v1 用 clean_text() 函数遍历标点清单，把标点替换为空格。
- 参考：Python 官方文档关于 str.replace 和 str.split 的说明。

四栏小结：
- 见 four_column_summary_w5.md

独立性自问：
- 见 independence_self_check_w5.md

下周计划：
- 学习文件读写与异常处理。
- 把 word_freq.py 改为从文件读取文章。
- 加入 try/except 处理文件不存在和编码问题。