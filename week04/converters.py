# W4 Day4: 换算模块
# 这个文件只负责"计算"，不负责"输入输出"
# 每个函数都是纯函数：给一个数，返回一个数

def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9 / 5 + 32

def kilometers_to_miles(kilometers):
    """公里转英里"""
    return kilometers * 0.621371

def kilograms_to_pounds(kilograms):
    """千克转磅"""
    return kilograms * 2.20462