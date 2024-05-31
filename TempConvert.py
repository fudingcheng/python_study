# 温度格式转换

# 接受用户输入的温度值
tempStr = input("请输入温度值,并以特定的符号结尾:")
# 判断用户输入的温度值是哪种类型
endStr = tempStr[-1]
# 如果输入的温度以C或c结尾
if endStr in ['C', 'c']:
    # 使用eval()将温度字符串转换为数字类型
    F = (eval(tempStr[0:-1]) * 1.8 + 32)
    print("转换后的温度是{:.2f}C".format(F))
# 如果输入的温度以F或f结尾
elif endStr in ['F', 'f']:
    C = (eval(tempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}F".format(C))
# 以上输入都不是的话,提示输入错误
else:
    print("您输入的格式有误!请重新输入")
