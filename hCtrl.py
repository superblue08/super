#!/usr/bin/python3
#!/usr/bin/python3
import sys

from tkinter import *
from tkinter import ttk

class Test(Tk):
    def __init__(self):
        super().__init__()
        self.title("This is a TEST!!!!")
        self.geometry("240x200")
        
        # 新增按鈕，按下後關閉視窗
        self.close_button = Button(self, text="Close", command=self.close_window)
        self.close_button.pack(pady=20)

    def close_window(self):
        self.destroy()  # 關閉視窗
        
if __name__ == "__main__":
    t = Test()
    t.mainloop()