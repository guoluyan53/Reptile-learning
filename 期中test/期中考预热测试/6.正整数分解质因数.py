# 6.	问题：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
n = int(input('输入一个正整数：'))

lt = [] #创建一个列表用来存放遍历出来的因数
m=n

while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=n//i #记录下用最小因数分解后的n
            lt.append(str(i))
            break

if len(lt) == 1:
    print(m,'=','1*',m)
else:
    s = 'x'.join(lt)
    print(m,'=',s)
