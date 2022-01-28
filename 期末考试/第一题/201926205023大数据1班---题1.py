#201926205023_郭禄燕 大数据1班
#第一题 获取个人学号尾号对应的章节（3）
import tkinter as tk
from bs4 import BeautifulSoup

# 解析html，获取文章标题
text = []  #存储文章
link = []  #存储链接
path = 'sanguo.html'
htmlfile = open(path, 'r', encoding='utf-8')
html = htmlfile.read()
soup = BeautifulSoup(html, 'lxml')
# 找到相应的标题内容
div = soup.findAll(name="div", attrs={"class": "book-mulu"}) #这里返回的是一个数组
li = div[0].findAll(name="li")  #获取
# print(li)
lilength = len(li)
for i in range(2,lilength,10):
    text.append(li[i].text) #将标题添加到数组
    lilink = 'https://www.shicimingju.com'+li[i].a.get("href")
    link.append(lilink) #将链接添加到数组
    # print(i)

# 将文章和链接映射为一个键值对
dictionary = dict(zip(text, link))

window = tk.Tk()
window.title('my window')
# 窗口尺寸
window.geometry('400x550')
# 创建一个lable
var1 = tk.StringVar()  #创建变量
l = tk.Label(window, bg='green', width=50, textvariable=var1)
l.pack()
# 按钮事件
def get_link():
    value = lb.get(lb.curselection())
    vallink = dictionary[value]  #根据选中的text去寻找对应的键值对
    var1.set(vallink)


# 创建一个按钮
btn = tk.Button(window, text='获取链接', width=10, height=2, command=get_link)
btn.pack()
# 创建一个Listbox和变量var2，并把var2的值赋给Listbox
var2 = tk.StringVar()
var2.set(text)

# 创建Listbox
lb = tk.Listbox(window, listvariable=var2, width=50, height=25)  #将var2的值赋值给Listbox
for item in text:
    lb.insert('end', item)  #从后面开始加入值
lb.pack()

# 显示
window.mainloop()