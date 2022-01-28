import tkinter as tk

window = tk.Tk()
window.title('my window')
##窗口尺寸
window.geometry('300x350')
#新建画布
canvas=tk.Canvas(window,bg='blue',height=150,width=300)

#画线
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
#画⚪
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
#画一个扇形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=90)
#画一个矩形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   
canvas.pack()
#创建文本框
entry = tk.Entry(window, show=None)
entry.pack()
#创建文本
label = tk.Label(window , text='圆：oval;线：line;扇形：arc;矩形 ：rect')
label.pack()  #打包
#向下移动
def moveit(event):
    obj = entry.get()  #获取输入框的参数，移动那个图形
    if obj =='rect':
        canvas.move(rect,0,2)  #第一个参数是图形
    elif obj == 'arc':
        canvas.move(arc, 0, 2)  # 第一个参数是图形
    elif obj =='oval':
        canvas.move(oval, 0, 2)  # 第一个参数是图形
    elif obj == 'line':
        canvas.move(line, 0, 2)

#向上移动
def moveup(event):
    obj = entry.get()  # 获取输入框的参数，移动那个图形
    if obj =='rect':
        canvas.move(rect,0,-2)  #第一个参数是图形
    elif obj == 'arc':
        canvas.move(arc,0,-2)  # 第一个参数是图形
    elif obj =='oval':
        canvas.move(oval,0,-2)  # 第一个参数是图形
    elif obj == 'line':
        canvas.move(line,0,-2)

#向左移动
def moveleft(event):
    obj = entry.get()  # 获取输入框的参数，移动那个图形
    if obj =='rect':
        canvas.move(rect, -2 ,0)  #第一个参数是图形
    elif obj == 'arc':
        canvas.move(arc, -2 ,0)  # 第一个参数是图形
    elif obj =='oval':
        canvas.move(oval, -2 ,0)  # 第一个参数是图形
    elif obj == 'line':
        canvas.move(line, -2, 0)

#向右移动
def moveright(event):
    obj = entry.get()  # 获取输入框的参数，移动那个图形
    if obj =='rect':
        canvas.move(rect,2,0)  #第一个参数是图形
    elif obj == 'arc':
        canvas.move(arc, 2,0)  # 第一个参数是图形
    elif obj =='oval':
        canvas.move(oval, 2,0)  # 第一个参数是图形
    elif obj == 'line':
        canvas.move(line , 2, 0)

#创建一个Button
b=tk.Button(window,text='下',command=moveit)
b.place(x=120,y=280)
# b.pack()
up=tk.Button(window,text='上',command=moveup)
# up.pack()
up.place(x=120,y=220)
left=tk.Button(window,text='左',command=moveleft)
left.place(x=80,y=250)
# left.pack()
right=tk.Button(window,text='右',command=moveright)
right.place(x=160,y=250)
# right.pack()

# 实现键盘绑定
window.bind("<KeyPress-Down>", moveit)  #第二个参数传一个回调函数
window.bind("<KeyPress-Left>", moveleft)
window.bind("<KeyPress-Right>", moveright)
window.bind("<KeyPress-Up>", moveup)
##显示出来
window.mainloop()