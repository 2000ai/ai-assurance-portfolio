# Day2: while 循环练习

# 1. 打印 1 到 10
count = 1
while count <= 10:
    print(count)
    count += 1  # 关键：不要忘记这行，否则死循环

# 2. 1 到 10 求和
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"1 到 10 的和是：{total}")

# 3. 用户输入 quit 退出（引入 break）
while True:
    user_input = input("请输入内容（输入 quit 退出）：")
    if user_input == "quit":
        print("程序退出。")
        break
    else:
        print(f"你输入了：{user_input}")