# Day3: for 循环练习

# 1. 打印 1 到 10
# 思考：为什么是 range(1, 11) 而不是 range(1, 10)？
print("=== 打印 1 到 10 ===")
for i in range(1, 11):
    print(i)

# 2. 求 1 到 100 的和
total = 0
for i in range(1, 101):
    total += i
print(f"1 到 100 的和是：{total}")

# 3. 倒序打印 10 到 1
print("=== 倒序打印 10 到 1 ===")
for i in range(10, 0, -1):
    print(i)

# 4. 验证 range 的边界（审计思维：自己验证，不靠猜）
print("=== 验证 range 边界 ===")
print("range(1, 5) 输出：")
for i in range(1, 5):
    print(i, end=" ")
print()  # 换行