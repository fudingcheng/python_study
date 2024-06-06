# 文本进度条
import time

scale = 10
print("{:=^20}".format("执行开始"))
start = time.perf_counter()
for i in range(scale + 1):
    # print(i)
    a = "*" * i  # *的数量
    b = "." * (scale - i)  # .的数量
    c = (i / scale) * 100
    d = time.perf_counter() - start
    time.sleep(0.5)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, d), end="")
print()
print("{:=^20}".format("执行结束"))
