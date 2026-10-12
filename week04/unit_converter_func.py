# W4 Day5: 单位换算器 函数版
import converters

def get_float(prompt):
    """一个小助手：显示提示，拿到用户输入，转成小数返回"""
    return float(input(prompt))

def main():
    print("=== 单位换算器 函数版 ===")

    celsius = get_float("请输入摄氏度：")
    fahrenheit = converters.celsius_to_fahrenheit(celsius)
    print(f"{celsius} 摄氏度 = {fahrenheit:.2f} 华氏度")

    kilometers = get_float("请输入公里数：")
    miles = converters.kilometers_to_miles(kilometers)
    print(f"{kilometers} 公里 = {miles:.2f} 英里")

    kilograms = get_float("请输入千克数：")
    pounds = converters.kilograms_to_pounds(kilograms)
    print(f"{kilograms} 千克 = {pounds:.2f} 磅")

    print("=== 换算完成 ===")

if __name__ == "__main__":
    main()