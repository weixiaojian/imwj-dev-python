#!/usr/bin/python3
# 1.基本数据类型
print("1.基本数据类型")
counter = 100
miles   = 1000.0
name    = "langao"
a = b = c = 1
print(a)
a, b, c = 1, 2, 3
print(a, b, c)
print("查看数据类型：", type(counter), type(miles), type(name))

# 2.数值运算
print("2.数值运算")
print(1 + 1)
print(4.3 - 2)
print(3 * 7)
print(2 / 4)
print(2 // 4)
print(17 % 3)
print(2 ** 3)

# 3.List
print("3.List")
list_data = ['a','b','c','d','e']
print(list_data)
print(list_data[0])
print(list_data[-1])
print(list_data[2:])
list_data[2] = "cc"
print(list_data)
list_data.append("FF")
print(list_data)

# 4.Tuple
print("4.Tuple")
tuple_data = (1,2,3)
print(tuple_data)

# 5.Set
print("5.Set")
print(list_data)
set_data = set(list_data)
print(set_data)
set_data.add("a")
set_data.add("b")
print(set_data)

# 6.Dictionary
print("6.Dictionary")
dict_data = {"name":"langao", "age": 28}
print(dict_data)
print(dict_data.keys())
print(dict_data.values())
print(dict_data.get("name"))

# 7.bytes
print("7.bytes")
x = b"hello"
print(x)
print(type(x))
print(x[0])