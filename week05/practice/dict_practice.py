# 1. 创建空字典
counts = {}
print("空字典：", counts)

# 2. 创建有初始值的字典
person = {"name": "AI审计师", "age": 1}
print("初始字典：", person)
# 3. 增加/修改（键不存在就是新增，存在就是修改）
counts["python"] = 1
counts["java"] = 1
print("增改后：", counts)

# 修改已有键的值
counts["python"] = 99
print("修改后：", counts)

# 4. 查（直接拿值）
print("python 的次数：", counts["python"])

# 5. 删除
del counts["java"]
print("删除后：", counts)

# 6. 判断键是否存在
print("python 在字典里吗？", "python" in counts)
print("java 在字典里吗？", "java" in counts)