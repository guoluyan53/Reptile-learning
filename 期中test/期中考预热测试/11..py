# 11.	问题：从键盘输入一些字符
# ，逐个把它们写到磁盘文件上，直到输入一个 # 为止

# filename = input("请输入文件名：")
# fp = open(filename, 'w')
# ch = input("请写入字符串：")
#
# while ch != '#':
#     fp.write(ch)
#     ch = input()
#
# fp.close()


# str.upper()  转化为大写
str = input('输入字符串：')
strchange = str.upper()
print(strchange)