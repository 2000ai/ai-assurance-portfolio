# W5 独立性自问

1. 我是否独立选择字典做计数？是。因为字典是键值映射，键唯一，天然去重。
2. 我是否理解为什么不用列表直接计数？是。列表查找慢，且无法直接去重。
3. 我是否理解 dict.get(word, 0) + 1？是。它先尝试取值，取不到就用 0 兜底，再加 1，避免 KeyError。
4. 我是否定义并写清了统计口径？是。路径：week05/evidence/counting_criteria_w5.md。
5. 我是否区分原始证据、中间证据、分析结果？是。见 evidence_chain_w5.md。
6. 我是否保留原始文章和终端输出？是。路径：week05/data/sample_article.txt 和 week05/evidence/terminal_output_w5.txt。
7. 我是否完成四栏小结且不缺失？是。路径：week05/logs/four_column_summary_w5.md。
8. 我是否卡壳超2小时才求助并记录 K 列？否。本次卡壳约 15 分钟，未超 2 小时。
9. 我是否没有删改原始错误记录？是。原始输出完整保留，没有删改。