#!/usr/bin/python3
import sys
import serial  # 新增匯入 serial 模組

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Test(Tk):
    def __init__(self):
        super().__init__()
        self.title("This is a TEST222!!!!")
        self.geometry("700x700")
        
        # 設定按鈕的固定寬度
        button_width = 20

        # 新增按鈕，按下後關閉視窗
        self.close_button = Button(self, text="Close", command=self.close_window, width=button_width)
        self.close_button.pack(pady=10)

        # 新增按鈕，按下後讀取檔案
        self.load_button = Button(self, text="Load File", command=self.load_file, width=button_width)
        self.load_button.pack(pady=10)

        # 新增按鈕，按下後透過 UART 傳送固定字串
        self.uart_button = Button(self, text="Send UART", command=self.send_uart, width=button_width)
        self.uart_button.pack(pady=10)

        # 新增按鈕，按下後接收 UART 訊息
        self.receive_uart_button = Button(self, text="Receive UART", command=self.receive_uart, width=button_width)
        self.receive_uart_button.pack(pady=10)

        # 新增按鈕，按下後將 UART 訊息存成文字檔
        self.save_uart_button = Button(self, text="Save UART Message", command=self.save_uart_message, width=button_width)
        self.save_uart_button.pack(pady=10)

        # 新增文字區域，用於顯示檔案內容
        self.text_area = Text(self, wrap=WORD, height=10, width=40)
        self.text_area.pack(pady=10)

        # 新增文字區域，用於顯示 UART 接收到的訊息
        self.uart_text_area = Text(self, wrap=WORD, height=10, width=40)
        self.uart_text_area.pack(pady=10)

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

    def send_uart(self):
        try:
            # 設定 UART 連線參數
            ser = serial.Serial(port='COM10', baudrate=2000000, timeout=1)  # 修改為實際的 UART 埠
            fixed_string = "Hello UART!"  # 固定字串
            ser.write(fixed_string.encode('utf-8'))  # 傳送字串
            ser.close()
            self.text_area.delete(1.0, END)
            self.text_area.insert(END, "UART message sent successfully!")
        except Exception as e:
            self.text_area.delete(1.0, END)
            self.text_area.insert(END, f"Error sending UART message: {e}")

    def receive_uart(self):
        try:
            # 設定 UART 連線參數
            ser = serial.Serial(port='COM10', baudrate=2000000, timeout=1)  # 修改為實際的 UART 埠
            received_data = ser.read(10).decode('utf-8')  # 接收最多 100 字元
            ser.close()
            self.uart_text_area.delete(1.0, END)
            self.uart_text_area.insert(END, received_data)  # 顯示接收到的訊息
        except Exception as e:
            self.uart_text_area.delete(1.0, END)
            self.uart_text_area.insert(END, f"Error receiving UART message: {e}")

    def save_uart_message(self):
        try:
            # 開啟檔案對話框讓使用者選擇儲存位置
            file_path = filedialog.asksaveasfilename(title="Save UART Message", defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.uart_text_area.get(1.0, END).strip()  # 取得 UART 訊息
                    file.write(content)
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, "UART message saved successfully!")
        except Exception as e:
            self.text_area.delete(1.0, END)
            self.text_area.insert(END, f"Error saving UART message: {e}")

if __name__ == "__main__":
    t = Test()
    t.mainloop()