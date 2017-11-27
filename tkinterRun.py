from tkinter import *
import tkinter as tk


class Application():
    def __init__(self, root):
        self.root = root
        self.root.bind("<KeyPress>", self.bind_key)
        self.root.bind("<KeyPress-Shift_R>", self.bind_r_key)

    def bind_key(self, event):
        print(event.keysym, " key is pressed")

    def bind_r_key(self, event):
        print("the right Shift key has been pressed")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("测试")
    Application(root)
    root.mainloop()