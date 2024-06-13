# 计算身体健康指标

height, weight = eval(input("请输入身高(米)和体重(kg)[用逗号隔开]:"))
bmi = weight / pow(height, 2)
nation, china = "", ""
if bmi < 18.5:
    nation, china = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    nation, china = "正常", "正常"
elif 24 <= bmi < 25:
    nation, china = "正常", "偏胖"
elif 25 <= bmi < 28:
    nation, china = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    nation, china = "偏胖", "肥胖"
else:
    nation, china = "肥胖", "肥胖"
normalWeightDown, normalWeightUp = pow(height, 2) * 18.5, pow(height, 2) * 24
print("您当前的BMI指标为:{:.1f},按照国际标准[{}],国内标准[{}]".format(bmi, nation, china))

if china == "偏胖" or china == "肥胖":
    print("按照国内标准建议您的体重保持在[{:.0f}kg~{:.0f}kg]这个健康水平".format(normalWeightDown, normalWeightUp))
