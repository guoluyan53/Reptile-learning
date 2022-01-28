import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

arrs=[] #用于第四题
#(1)随机产生1-6的整数
def rolls():
    roll = random.randint(1, 6)
    return roll

#(2)统计每两次骰子出现的次数
def two():
    arr = []
    x = rolls()
    y = rolls()
    arr.append(x)
    arr.append(y)
    return arr
#统计每两次的次数存入一个二维数组
def countci():
    arrtwo = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for i in range(50000):
        arr = two()
        x = arr[0]
        y = arr[1]
        arrs.append(x)
        arrs.append(y)
        arrtwo[x-1][y-1] += 1
    return arrtwo
#（2）画图
def img():
    arrtwo = countci()
    x = np.array([1, 2, 3, 4, 5, 6])
    y = np.array([1, 2, 3, 4, 5, 6])
    z = []
    for i in x:
        for j in y:
            z.append(arrtwo[i-1][j-1])
    X,Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter3D(X, Y, z)
    plt.show()


#(3) 打印2中生成的数组，检测是否含有差值小于50的两个元素
def chazhi():
    arrtwo = countci()
    print(arrtwo)
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for h in range(6):
                    if arrtwo[i][j]-arrtwo[k][h] < 50 and i != k and j != h:
                        print(str(i)+','+str(j)+','+str(arrtwo[i][j])+'--'+str(k)+','+str(h)+','+str(arrtwo[k][h]))
                    else:
                        print("没有")


#(4)将2中产生的所有骰子的数值写入一个文本data.txt
def write():
    with open('data.txt', 'w') as f:
        for i in arrs:
            f.write(str(i))


#a.如果每两次的骰子数字为7，则写入*x*y ,学号为奇数,写入文件为sum7.txt
def sum():
    flag = 0
    with open('sum7.txt', 'w') as f:
        for i in range(0, len(arrs), 2):
            if arrs[i]+arrs[i+1] == 7:
                strs = '*' + str(arrs[i]) + '*' +str(arrs[i+1])
                for j in strs:
                    if flag == 80:
                        f.write('\n')
                        flag = 0
                    f.write(j)
                    flag += 1
            else:
                strs = str(arrs[i]) + str(arrs[i+1])
                for j in strs:
                    if flag == 80:
                        f.write('\n')
                        flag = 0
                    f.write(j)
                    flag += 1


#5.读入data.txt，统计666出现的次数
def count666():
    f = open("data.txt", 'r')
    strr = f.read()
    print(strr.count('666'))

chazhi()
img()
write()
sum()
count666()
# print(countci())




