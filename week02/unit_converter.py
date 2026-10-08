# 单位换算器 v1
print("=== 单位换算器 v1 ===")

# 1. 摄氏度 -> 华氏度
celsius = float(input("请输入摄氏度："))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} 摄氏度 = {fahrenheit:.2f} 华氏度")

# 2. 公里 -> 英里
kilometers = float(input("请输入公里数："))
miles = kilometers * 0.621371
print(f"{kilometers} 公里 = {miles:.2f} 英里")

# 3. 千克 -> 磅
kilograms = float(input("请输入千克数："))
pounds = kilograms * 2.20462
print(f"{kilograms} 千克 = {pounds:.2f} 磅")

print("=== 换算完成 ===")