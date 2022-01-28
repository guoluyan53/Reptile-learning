#模拟50000次扔两个骰子，显示两个骰子点数之和为8的次数占总次数的比例
import random
#投骰子的点数
def rolls():
    roll = random.randint(1,6)
    return roll

def tou():
    num = 0
    for i in range(50000):
        n1 = rolls()
        n2 = rolls()
        if n1+n2==8:
            num=num + 1
    return num

numf=tou()
print(numf)
b = float(50000)
print("%.1f%%"%(numf/b*100))
