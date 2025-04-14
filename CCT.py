#!/usr/bin/python3
import sys

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Test(Tk):
    def __init__(self):
        super().__init__()
        self.title("This is a TEST!!!!")
        self.geometry("400x300")
        
        # 新增按鈕，按下後關閉視窗
        self.close_button = Button(self, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

        # 新增按鈕，按下後讀取檔案
        self.load_button = Button(self, text="Load File", command=self.load_file)
        self.load_button.pack(pady=10)

        # 新增文字區域，用於顯示檔案內容
        self.text_area = Text(self, wrap=WORD, height=10, width=40)
        self.text_area.pack(pady=10)

    def close_window(self):
        self.destroy()  # 關閉視窗

    def load_file(self):
        # 開啟檔案對話框讓使用者選擇檔案
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, END)  # 清空文字區域
                    self.text_area.insert(END, content)  # 顯示檔案內容
            except Exception as e:
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, f"Error reading file: {e}")

if __name__ == "__main__":
    t = Test()
    t.mainloop()