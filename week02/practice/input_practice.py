# Day2: input 与 print 练习
name = input("请输入你的名字：")
print("你好，", name)
print(f"你好，{name}")

age = input("请输入年龄：")
print(type(age))   # 关键点：input 永远返回字符串 str