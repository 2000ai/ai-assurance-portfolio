# Day1: 函数基础练习

# 1. 简单的加法函数
def add(a, b):
    return a + b

# 2. 判断偶数
def is_even(number):
    return number % 2 == 0

# 3. 带默认参数的函数
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

# 4. 多返回值（返回一个元组）
def min_max(numbers):
    return min(numbers), max(numbers)

# === 测试 ===
print("3 + 5 =", add(3, 5))
print("10 是偶数吗？", is_even(10))
print(greet("审计师"))
print(greet("审计师", "早上好"))

low, high = min_max([3, 1, 7])
print(f"最小值：{low}，最大值：{high}")