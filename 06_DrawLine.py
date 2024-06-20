# 绘制数码管案例
import turtle,time


def drawGap():
    turtle.penup()
    turtle.fd(5)


# 绘制一条线
def drawLine(ifDraw):
    drawGap()
    turtle.pendown() if ifDraw else turtle.penup()
    turtle.fd(40)
    # 每次画完后画笔右转90°
    drawGap()
    turtle.right(90)


# 根据对应数字绘制一个数码管
def drawDigit(digit):
    # 绘制第一条线
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    # 绘制第二条线
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    # 绘制第三条线
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8] else drawLine(False)
    # 绘制第四条线
    drawLine(True) if digit in [0, 2, 5, 6, 8] else drawLine(False)

    # 画笔左转90°
    turtle.left(90)

    # 绘制第五条线
    drawLine(True) if digit in [0, 1, 4, 5, 6, 8, 9] else drawLine(False)

    # 绘制第六条线
    drawLine(True) if digit in [0, 2, 3, 5, 7, 8, 9] else drawLine(False)

    # 绘制第七条线
    drawLine(True) if digit in [0, 1, 2, 3, 4, 5, 7, 8, 9] else drawLine(False)

    # 画笔转向180°
    turtle.right(180)
    # 画笔向前移动,为下个数字做准备
    turtle.penup()
    turtle.fd(20)


# 根据输入的数字绘制制定的数码管
def drawNumber(number):
    turtle.pencolor('red')
    for i in number:
        if i == '-':  # 绘制年
            turtle.write('年', font=('阿里巴巴普惠体', 30, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '+':
            turtle.write('月', font=('阿里巴巴普惠体', 30, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '=':
            turtle.write('日', font=('阿里巴巴普惠体', 30, 'normal'))
        else:
            drawDigit(eval(i))


# 主函数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-340)
    turtle.pensize(5)
    # drawNumber("20240620")
    drawNumber(time.strftime('%Y-%m+%d='))
    turtle.hideturtle()
    turtle.done()


main()
