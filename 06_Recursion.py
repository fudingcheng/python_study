# 递归
'''
    递归就是函数调用自身
    递归的编程实现 = 函数+分支语句
    递归的实现步骤:
        1. 定义一个函数
        2. 确定基例,基例中返回确定的值
        3. 确定链条,链条中递归调用
'''


# 用递归计算阶乘
def fact(n):
    if n == 0:  # 基例
        return 1
    else:
        return n * fact(n - 1)  # 链条


# print(fact(5))

# 用递归实现字符串反转
def reverseStr(str):
    if str == '':  # 基例
        return str
    else:
        return reverseStr(str[1:]) + str[0]  # 链条


# print(reverseStr("abcdefg"))


# 用递归实现斐波那契数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10))


# 用递归实现汉诺塔,把n个元素从a移动到b
count = 0  # 定义全局变量,用来记录移动次数


def hanoi(n, src, dest, mid):
    global count  # 声明全局变量,代表要使用它
    if n == 1:  # 如果只有一个元素,直接从src挪到dest
        print("{}:{}->{}".format(1, src, dest))
        count += 1
    else:  # 如果超过1个元素,按照下面的步骤来移动
        hanoi(n - 1, src, mid, dest)  # 第一步: 先把n-1个元素(想象成一个整体)从src挪到mid上(以dest为过渡),目的是给第n个元素腾出空间
        print("{}:{}->{}".format(n, src, dest))  # 第二步: 把第n个元素从src直接挪到dest上
        count += 1
        hanoi(n - 1, mid, dest, src)  # 第三步: 再把第n-1个元素从mid上挪到dest上,以src为过渡
    return count


count = hanoi(3, "A", "C", "B")
print("一共移动了{}次".format(count))