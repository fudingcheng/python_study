# 进步算法

#  每天进步1%,与每天退步1%,365天后的差距
# dayFactor = 0.01
# dayUp = pow(1+dayFactor, 365)
# dayDown = pow(1-dayFactor, 365)
# print("天天向上:{:.2f},天天向下:{:.2f}".format(dayUp, dayDown))


# 每周一~周五进步1%,周六和周日休息退步0.5%
# day = 1
# dayFactor = 0.03
# for i in range(365):
#     if i % 7 in [6, 0]:  # 周六和周日
#         day *= (1 - dayFactor)
#     else:               # 周一到周五
#         day *= (1 + dayFactor)
# print("周内学习,周末休息,365天后{:.2f}".format(day))

# 定义一个方法,专门用来计算工作日的努力值
def dayUp(dayFactor):
    day = 1
    for i in range(365):
        if i % 7 in [6, 0]:  # 周六和周日
            day *= (1 - 0.01)
        else:  # 周一到周五
            day *= (1 + dayFactor)
    return day;


dayFactor = 0.01
everyDay = pow(1.01, 365)
while dayUp(dayFactor) < everyDay:
    dayFactor += 0.001
print("工作日努力,需要每天努力{:.3f}才能追赶上每天努力0.01的{:.3f}".format(dayFactor, everyDay))
