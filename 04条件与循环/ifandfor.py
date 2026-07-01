# 1.if条件控制
print("1.if条件控制")
a = 1
while a < 3:
    if (a % 2 == 0):
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1

age = int(input("请输入一个数字"))
if (age % 2 == 0):
    print(a, "is even")
else:
    print(a, "is odd")

# 2.match
print("2.match")
def http_error(status):
    match status:
        case 200:
            return ("success")
        case 404:
            return ("not found")
        case 501|502:
            return ("501 or 502")
        case _:
            return ("error")
print(http_error(200))
print(http_error(404))
print(http_error(501))

# 3.while
print("3.while")
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

# 4.for
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)
else:
    print("Finally finished!")

# 5.break and continue
print("5.break and continue")
n = 5
while n > 0:
    n -= 1
    if n == 3:
        continue
    if n == 2:
        break
    print(n)

# 6.pass语句
for letter in "Python":
    if letter == "t":
        pass
        print("执行pass")
    print(letter)

