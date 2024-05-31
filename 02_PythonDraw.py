# 使用turtle画蟒蛇

# 导入turtle
import turtle

# 设置窗体
turtle.setup(650, 320)

# 1. 画笔的准备工作
# 抬起画笔
turtle.penup()
# 设置画笔的起始位置
turtle.fd(-250)
# 调整画笔的角度
turtle.seth(-40)
# 设置画笔的大小
turtle.pensize(20)
# 设置画笔的颜色
turtle.pencolor("red")
# 放下画笔,准备画画
turtle.pendown()

# 2. 画蟒蛇的主体部分
# 设置循环
for i in range(4):
    # 蟒蛇的身体部分
    turtle.circle(40,80)
    turtle.circle(-40,80)
# 蟒蛇的回头效果
turtle.seth(0)
turtle.fd(10)
turtle.circle(20,180)
turtle.fd(30)

# 3. 让窗体一直保持不消失
turtle.done()
