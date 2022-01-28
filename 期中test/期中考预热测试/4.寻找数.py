# 4.	问题：一个整数（小于1000），它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？
import math

def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n

for i in range(1000):
    if i%10 in [0,1,4,5,6,9]:
        if isSqr(i+100) and isSqr(i+268):
            print(i)