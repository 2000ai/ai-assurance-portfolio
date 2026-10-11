# Day4: 猜数字 v0（固定答案，无限循环直到猜对）
answer = 7

while True:
    guess = int(input("猜一个 1-10 的数字："))

    if guess == answer:
        print("猜对了！")
        break  # 关键：猜对后立刻跳出死循环
    elif guess < answer:
        print("小了")
    else:
        print("大了")