# -*- coding: utf-8 -*-


import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from tkinter import Menu, ttk


win = tk.Tk()
win.title("Python GUI")    # 添加标题


def _quit():
    """结束主事件循环"""
    win.quit()      # 关闭窗口
    win.destroy()   # 将所有的窗口小部件进行销毁，应该有内存回收的意思
    exit()


def _open():
    filename = tkinter.filedialog.askopenfilename(filetypes=[("bmp格式", "bmp")])


def go(*args):  # 处理事件，*args表示可变参数
    print(comboxlist.get())  # 打印选中的值
    tkinter.messagebox.showinfo(title='callback', message=comboxlist.get())


# 创建菜单栏功能
menuBar = Menu(win)
win.config(menu=menuBar)


# 创建一个名为File的菜单项
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

# 在菜单项File下面添加一个名为New的选项
fileMenu.add_command(label="New",command=_open)

# 在两个菜单选项中间添加一条横线
fileMenu.add_separator()

# 在菜单项下面添加一个名为Exit的选项
fileMenu.add_command(label="Exit", command=_quit)

# 在菜单栏中创建一个名为Help的菜单项
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)

# 在菜单栏Help下添加一个名为About的选项
helpMenu.add_command(label="About")

comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
comboxlist["values"] = ("1", "2", "3", "4")
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.pack()

win.mainloop()      # 进入主事件循环，当调用mainloop()时,窗口才会显示出来
