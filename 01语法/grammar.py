#!/user/bin/python3
# 1.变量定义
print("1.变量定义：")
age = 25
user_name = "langao"
_total = 100
MAX_SIZE = 1024


# 2.方法定义（语法检测）
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print("2.方法定义（语法检测）：")
print(is_valid_identifier(user_name))
print(is_valid_identifier("2var"))


# 3.注释
# ------------

# 连续
# 多行
# 注释

'''
多行注释
'''

"""
多行注释
"""

# 4.行与缩进
print("4.行与缩进：")
if True:
    print("True")
else:
    print("False")

# 5.多行语句
print("5.多行语句：")
total = user_name + \
        "123" + \
        "456"
print(total)

# 6.数据类型
print("6.数据类型：")
# 数字类型
int_data = 1;
bool_data = True;
float_data = 1.23;
complex_data = complex(1, 2);
# 字符串类型
word_data = '字符串'
sentence_data = "这是一个句子"
paragraph_data = """这是一个段落：
                段落一，
                段落二。"""
str_data = "123456789"
print(int_data)
print(bool_data)
print(float_data)
print(complex_data)
print(word_data)
print(sentence_data)
print(paragraph_data)

print(str_data)
print(str_data[0])

print("hello \n runoob"); print(r"hello \n runoob")

# 7.用户输入
print("7.用户输入：")

input("\n\n 按下enter键后退出")


# 8.import or from...import
print("8.import or from...import")
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 9.命令行参数
print("9.命令行参数")
'''
$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit

[ etc. ]
'''
