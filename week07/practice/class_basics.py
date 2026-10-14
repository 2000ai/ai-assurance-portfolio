# W7 Day1: 类与对象基础练习

# 1. Dog 类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} 在叫"


# 2. FileInfo 类
class FileInfo:
    def __init__(self, name, ext, size):
        self.name = name
        self.ext = ext
        self.size = size

    def describe(self):
        return f"文件 {self.name}，类型 {self.ext}，大小 {self.size} 字节"


# 3. 测试 Dog 类
dog = Dog("旺财", 3)
print("名字：", dog.name)
print("年龄：", dog.age)
print("叫声：", dog.bark())

# 4. 测试 FileInfo 类
file1 = FileInfo("report.pdf", ".pdf", 2048)
print(file1.describe())