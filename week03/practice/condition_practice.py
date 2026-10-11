# Day1: 条件判断练习

# 1. 判断奇偶
number = int(input("请输入一个整数："))
if number % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")

# 2. 判断成绩等级
score = float(input("请输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")