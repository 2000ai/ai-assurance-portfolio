# W5 证据链

## 一、原始证据
- 文章原文：week05/data/sample_article.txt
- 脚本源码：week05/word_freq.py
- Git commit：（提交后补充你的 commit hash）

## 二、中间证据
- 清洗后的词列表：由脚本的 clean_text() 和 get_words() 生成
- 计数字典：由 count_words() 生成
- 排序后的列表：由 sort_counts() 生成
（*注：W6 学文件读写后，我们会把中间结果打印到文件里留存*）

## 三、分析结果
- 总词数：17
- 唯一词数：9
- Top 10 高频词：
  - python: 6
  - is: 4
  - great: 1
  - easy: 1
  - learning: 1
  - fun: 1
  - powerful: 1
  - and: 1
  - friendly: 1
- 终端输出留档：week05/evidence/terminal_output_w5.txt

## 四、复现步骤（别人怎么验证你的结果）
1. 进入项目目录：`cd ~/ai-assurance-portfolio`
2. 激活环境：`conda activate ai-assurance`
3. 运行脚本：`python week05/word_freq.py`
4. 对照本文件“统计口径说明”和“分析结果”

## 五、结论
- 在本样本、本口径下，Top 10 高频词为上述列表。
- 该结果受样本大小、停用词、分词规则限制，不能外推到其他语料。