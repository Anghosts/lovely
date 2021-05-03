from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Hello")  # 窗口标题

# 参数：(窗口的长x宽+距屏幕左边的宽度+距屏幕上边的宽度)
# + 表示左边，- 表示右边
root.geometry("500x400+500+300")

btn01 = Button(root)
btn01["text"] = "点我"

btn01.pack()


def songhua(e):
    messagebox.showinfo("Message", "送你一朵花")


btn01.bind("<Button-1>", songhua)

root.mainloop()
