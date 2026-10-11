# Day6: 猜数字 v2（限制次数）
import random

answer = random.randint(1, 100)
max_attempts = 7
count = 0
guess = None  # 先初始化，避免循环结束后变量未定义

print("我想了一个 1-100 的数字，你有 7 次机会。")

while count < max_attempts:
    guess = int(input("请输入你的猜测："))
    count += 1

    if guess < answer:
        print("小了")
    elif guess > answer:
        print("大了")
    else:
        print(f"猜对了！你用了 {count} 次。")
        break

# 循环结束后的判断：如果最后一次猜测不等于答案，说明次数用完了
if guess != answer:
    print(f"机会用完，答案是 {answer}。")