# Day5: 猜数字 v1（随机答案 + 次数统计）
import random

answer = random.randint(1, 100)
count = 0

print("我想了一个 1-100 的数字。")

while True:
    guess = int(input("请输入你的猜测："))
    count += 1

    if guess < answer:
        print("小了")
    elif guess > answer:
        print("大了")
    else:
        print(f"猜对了！你用了 {count} 次。")
        break  # 猜对后跳出循环