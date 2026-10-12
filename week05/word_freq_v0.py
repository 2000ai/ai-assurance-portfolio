# W5 Day4: 词频统计 v0（最简版）
# 目标：先跑通，暴露问题，不追求完美

ARTICLE = """
Python is great. Python is easy. Learning Python is fun.
Python is powerful and Python is friendly.
"""

# 1. 转小写，再按空白切分成列表
words = ARTICLE.lower().split()

# 2. 用字典统计频次
counts = {}
for word in words:
    # 用 get 安全取值，不存在就当 0，再加 1
    counts[word] = counts.get(word, 0) + 1

# 3. 遍历字典，打印每个词和次数
for word, count in counts.items():
    print(word, count)