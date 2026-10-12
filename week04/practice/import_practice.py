# W4 Day3: 作用域与 import 练习

# 1. 全局变量
x = 10

def show_scope():
    # 2. 局部变量
    y = 5
    print("函数内能看到全局 x =", x)
    print("函数内能看到局部 y =", y)

show_scope()

# 函数外部看不到局部变量 y
# print(y)   # 取消注释会报 NameError

# 3. import 练习
import math

print("用 import 调用 math.sqrt(16) =", math.sqrt(16))

from math import sqrt
print("用 from import 调用 sqrt(16) =", sqrt(16))

import math as m
print("用别名调用 m.sqrt(16) =", m.sqrt(16))