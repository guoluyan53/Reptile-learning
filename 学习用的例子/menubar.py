import tkinter as tk

window = tk.Tk()
window.title('my window')
##窗口尺寸
window.geometry('200x200')
#新建一个label
l=tk.Label(window,text='',bg='yellow')
l.pack()
#计数
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
#创建菜单
menubar=tk.Menu(window)
#菜单一
filemenu=tk.Menu(menubar,tearoff=0)
#一级菜单
menubar.add_cascade(label='File',menu=filemenu)
#二级菜单
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_separator()#分割线
filemenu.add_command(label='Exit',command=window.quit)
#菜单二
editmenu=tk.Menu(menubar,tearoff=0)
#一级菜单
menubar.add_cascade(label='Edit',menu=editmenu)
#二级菜单
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Paste',command=do_job)
#
#菜单一子菜单
submenu=tk.Menu(filemenu)
#一级菜单
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
#二级菜单
submenu.add_command(label='Submeau1',command=do_job)
submenu.add_command(label='Submeau1',command=do_job)

window.config(menu=menubar)
##显示出来
window.mainloop()