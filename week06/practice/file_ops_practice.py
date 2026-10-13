# W6 Day1: 文件读写基础练习

# 1. 用 w 模式写入三行
with open("week06/data/sandbox/normal.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
print("写入完成。")

# 2. 用 r 模式读取全部内容
with open("week06/data/sandbox/normal.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("=== 读取全部内容 ===")
print(content)

# 3. 用 a 模式追加一行
with open("week06/data/sandbox/normal.txt", "a", encoding="utf-8") as f:
    f.write("追加的第四行\n")
print("追加完成。")

# 4. 逐行读取
print("=== 逐行读取 ===")
with open("week06/data/sandbox/normal.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("行内容：", line.strip())