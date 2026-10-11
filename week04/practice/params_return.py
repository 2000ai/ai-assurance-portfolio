# 1. 位置参数
def power(base, exponent):
    # ** 是幂运算，base 的 exponent 次方
    return base ** exponent

# 调用时，2 对应 base，3 对应 exponent
print(power(2, 3))   # 输出 8

# 2. 关键字参数
# 这里我们故意打乱顺序，也不会出错
print(power(exponent=3, base=2))   # 输出 8

# 3. 默认参数
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"#重要规则：默认参数必须写在非默认参数后面

# 不传第二个参数，用默认的"你好"
print(greet("审计师"))               # 输出：你好，审计师

# 传了第二个参数，覆盖默认值
print(greet("审计师", "早上好"))     # 输出：早上好，审计师

# 4. 多返回值
def min_max(numbers):
    # min() 取最小值，max() 取最大值
    return min(numbers), max(numbers)

# 调用时，可以用两个变量分别接住这两个返回值（这叫"解包"）
low, high = min_max([3, 1, 7])
print(f"最小值：{low}，最大值：{high}")   # 输出：最小值：1，最大值：7