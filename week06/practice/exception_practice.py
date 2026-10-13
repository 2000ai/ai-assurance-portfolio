# W6 Day2: 异常处理练习

# 1. FileNotFoundError
try:
    with open("week06/data/不存在的文件.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError as e:
    print("捕获到 FileNotFoundError：文件不存在")
    print("错误信息：", e)

# 2. IsADirectoryError
try:
    with open("week06/data/sandbox", "r", encoding="utf-8") as f:
        content = f.read()
except IsADirectoryError as e:
    print("捕获到 IsADirectoryError：不能把目录当文件读")
    print("错误信息：", e)

# 3. UnicodeDecodeError
try:
    with open("week06/data/sandbox/gbk_file.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError as e:
    print("捕获到 UnicodeDecodeError：编码不匹配")
    print("错误信息：", e)

# 4. 兜底 Exception
try:
    number = int("abc")
except Exception as e:
    print("兜底捕获：", type(e).__name__, "-", e)

# 5. finally
try:
    print("尝试打开文件...")
    with open("week06/data/sandbox/normal.txt", "r", encoding="utf-8") as f:
        print("文件内容长度：", len(f.read()))
except FileNotFoundError as e:
    print("文件不存在：", e)
finally:
    print("=== 无论成功失败，这句都会执行 ===")