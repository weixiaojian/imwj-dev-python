#!/usr/bin/python3
# 1.打印字符串
print("Hello World")

# 2.输出变量
i = 256 * 256
print("i的值为：", i)

# 3.数学运算
x = 3
y = 6
print(x + y)

# 4.列表
my_list = ["claude code", "codex", "Cursor"]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 5.for循环
for i in range(3):
    print(i)

# 6.while
i = 10
while i > 0:
    print(i)
    i = i - 1

# 7.end关键字
a, b = 0,1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b