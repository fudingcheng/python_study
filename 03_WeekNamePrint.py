# 根据用户输入的数字输出对应星期

weekStr = "一二三四五六七"
num = eval(input("请输入1-7之间的一个数组:\n"))
if num in range(1, 7):
    print("星期"+weekStr[num-1])
else:
    print("你的输入有误")