#################################### [Python基本数据类型] ######################################################

# n = pow(10,-16)
# print(n)

# n=0x101
# print(n)

# n_1 = 0.1 + 0.2 == 0.3  # false
# n_2 = round(0.1 + 0.2, 1) == 0.3 # true
# print(n_2)

# z=123e-4+5.6e+89j
# print(z.real)
# print(z.imag)

# print(10 // 3)
# print(10 % 3)
#
# print(2**0.5)
#
# print(divmod(1,3))
#
# print(complex(10).real)

# 取模其实就是把数据按照制定的宽度分组
# for i in range(1, 366):
#     if i % 4 in [0]:
#         print(i)

# print("'''")
# print('"""')

# str = "1234567890"
# print(str[0:-1:2])
# print(str[0::2])
# print(str[:-1:2])


# print("\"")  # 转义符
# print("1234567\b")  # 123456      回退
# print("1234567\r890")  # 890      覆盖
# print("1234567\n123")  # 换行      换行

# print("123" * 8)
# print("1" in "123")
# print(len(str(123)))

# print(ord("a"))

# print(chr(9800))

# print("abc".upper().lower())
# print("a,b,c".split(","))
# print("aabc".count("a"))
# print("abc".replace("a", "A"))
# print("abc".center(9, "="))
# print("=python=".strip("=np"))
# print(",".join("abc"))
#
# # 字符串的格式化输出
# print("{:=^20}".format("python"))
# print("{:,.2f}".format(12345.6789))
#
# # 导入时间模块
# import time
#
# print(time.time())
# print(time.ctime())
# print(time.gmtime())
# t = time.gmtime()
# print(time.strftime("%Y-%m-%d,%H:%M:%S", t))
#
# str = "2024-06-06,09:20:44"
# print(time.strptime(str, "%Y-%m-%d,%H:%M:%S"))
#
# print("=" * 20)
# start = time.perf_counter()
# time.sleep(2)
# end = time.perf_counter()

# print(end-start)

###################################### [程序的控制结构] ####################################################

# guess = eval(input("请输入一个数:"))
# if guess == 99:
#     print("猜对了")
# else:
#     print("猜错了")

# 二分结构的紧凑写法
# print("猜{}了".format("对" if guess == 99 else "错"))

# if guess == 99:
#     print("猜对了")
# elif guess > 100:
#     print("不要超过100")
# else:
#     print("猜错了")

# try:
#     guess = eval(input("请输入一个数:"))
#     print(guess * 2)
# except SyntaxError:
#     print('输入的不是整数')
# else:
#     print("else在不发生异常时执行")
# finally:
#     print("finally一定执行")

# for n in range(10):
#     print("Hello:", n)
#
# print("=" * 20)
#
# for n in range(2, 11, 2):
#     print("Hello:", n)
#
# print("=" * 20)
#
# for c in "Python123":
#     print(c, end=",")
#
# print()
# print("=" * 20)
#
# for item in [123, "python", 456]:
#     print(item, end=",")
#
# print()
# print("=" * 20)
#
# a = 3
# while a > 0:
#     a = a - 1
#     print(a)
#
# print()
# print("=" * 20)
#
# for c in "python":
#     if c == "t":
#         # continue
#         break
#     print(c, end="")
#
# print()
# print("=" * 20)
#
# s = "python"
# while s != "":
#     for c in s:
#         if c == "t":
#             break
#         print(c, end="")
#     s = s[:-1]
#
# print()
# print("=" * 20)

# for c in "Python":
#     if c == "t":
#         break
#         # continue
#     print(c, end="")
# else:
#     print("正常退出")
#
# print()
# print("=" * 20)
#
# import random
#
# print(random.random())

# 设置种子
# random.seed(10)
# print(random.random())
#
# print()
# print("=" * 20)
#
# print(random.randint(1, 10))  # 生成1-10之间的随机数
# print(random.randrange(1, 10, 2))  # 生成1-10之间,步长为2的随机数
# print(random.getrandbits(16))  # 生成16个字节长度的随机数
# print(random.uniform(10, 100))  # 生成10~100之间的小数
#
# print()
# print("=" * 20)
#
# print(random.choice([1, 2, 3, 4, 5]))  # 从序列中随机选择一个元素
# print()
# print("=" * 20)
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# random.shuffle(s)
# print(s)

########################################### [函数和代码的复用] ###############################################

'''n的阶乘'''

# 定义函数
# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
#
#
# print(fact(10))

# 非必须参数
# def fact(n, m=1):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result // m
#
#
# print(fact(10, 5))

# 可变参数,返回多个参数
# def fact(n, *b):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     for i in b:
#         result *= i
#     return result, result // 5, result // 3


# print(fact(10, 5, 4, 3, 2, 1))

# a, b, c = fact(10, 5, 4)
# print(a, b, c)

# 局部变量和全局变量
a = 123


def func():
    # a = 456
    global a
    a += 1
    print(a)


func()


########################################### [lambda] ###############################################

# f = lambda x, y: x + y
# print(f(1, 2))
#
# p = lambda: "lambda函数"
# print(p())

# 递归
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
