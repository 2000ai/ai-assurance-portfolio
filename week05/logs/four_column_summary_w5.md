# W5 四栏小结

## 发现
- 完成词频统计脚本，能输出总词数、唯一词数、Top 10。
- 发现未排除停用词时，is、and 等会进入高频。
- 发现标点未清洗时，python. 和 python 会分开。
- 发现中文不能按空格简单分词。

## 证据
- 原始文章：week05/data/sample_article.txt
- 脚本：week05/word_freq.py
- 终端输出：week05/evidence/terminal_output_w5.txt
- 口径说明：week05/evidence/counting_criteria_w5.md
- 证据链：week05/evidence/evidence_chain_w5.md
- Git commit：b1ac6e6

## 风险
- 样本太小，结论不能外推。
- 停用词未排除，高频词可能不代表主题。
- 未做词形还原，is/are、run/running 分开。
- 中文分词缺失，中文文章结果不可靠。
- 口径若变化，结果不可比。

## 建议
- W6 改为读取文件，并加异常处理。
- 后续加停用词表。
- 后续加正则表达式处理标点。
- 中文文本引入 jieba 等分词工具。
- 固定统计口径模板，保证可比性。