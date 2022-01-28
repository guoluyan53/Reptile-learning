# 7.	问题：输入一行字符，分别统计出其中英文字母、空格、数字和其它字
# 符的个数。
# 例如：输入Hello world! 123 输出应该是：字母10 数字3 符号1.

str = input('请输入一个字符串：')
a=0,
b=0,
c=0
for i in str:
    if(i.isalpha()):
        a+=1
    elif(i.isdigit()):
        b+=1
    else:
        c+=1

print()
