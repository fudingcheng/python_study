# 使用递归实现科赫雪花算法
import turtle

'''
    size:线段长度
    n:科赫雪花图形的阶数
'''


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 800)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    turtle.hideturtle()


main()
