# W5 Day1: 列表基础练习

# 1. 创建
words = ["python", "is", "great", "python"]

# 2. 索引
print("第一个词：", words[0])
print("最后一个词：", words[-1])

# 3. 切片
print("前两个：", words[0:2])
print("从第 2 个到末尾：", words[1:])

# 4. 追加
words.append("easy")
print("追加后：", words)

# 5. 长度
print("列表长度：", len(words))

# 6. 判断存在
print("python 在列表里吗？", "python" in words)
print("java 在列表里吗？", "java" in words)

# 7. 遍历
print("=== 遍历列表 ===")
for word in words:
    print(word)

# 8. 排序
words.sort()
print("排序后：", words)