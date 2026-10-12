# W5 Day3: 字符串处理练习

# 原始文本（注意前后有空格，末尾有标点）
text = "  Python is great. Python is easy!  "
print("原始文本：", repr(text))  # repr 会显示原样，包括空格

# 1. 转小写
text_lower = text.lower()
print("转小写后：", repr(text_lower))

# 2. 去首尾空白
text_stripped = text_lower.strip()
print("去空白后：", repr(text_stripped))

# 3. 替换标点
text_replaced = text_stripped.replace(".", " ").replace("!", " ")
print("去标点后：", repr(text_replaced))

# 4. 切分成列表
words = text_replaced.split()
print("切分后词列表：", words)

# 5. 统计词数
print("总词数：", len(words))
print("前 10 个词：", words[:10])