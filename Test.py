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
print("1234567\r890")  # 890      覆盖
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
