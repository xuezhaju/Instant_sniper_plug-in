import tkinter as tk
import win32api
import win32con

'''
# 获取窗口句柄
hwnd = win32gui.FindWindow(None, "穿越火线")
#classname = win32gui.GetClassName(hwnd)

# 设置为前台窗口
win32gui.SetForegroundWindow(hwnd)
'''
#暂停tkinter的响应
def delay(root, delay_time):
    # 这里的代码会在指定的毫秒数后执行
    root.after(delay_time, delay, delay_time)

def down_left():
    # 设置鼠标位置
    win32api.SetCursorPos((100, 100))  # 假设您想要将鼠标移动到屏幕坐标(100, 100)

    # 模拟鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    # 模拟鼠标左键抬起
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def down_right():
    # 设置鼠标位置
    win32api.SetCursorPos((100, 100))  # 假设您想要将鼠标移动到屏幕坐标(100, 100)

    # 模拟鼠标右键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

    # 模拟鼠标右键抬起
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def make_window(w_name, w, h, x, y):
    w_name.overrideredirect(True)
    w_name.wm_attributes("-topmost", True)
    w_name.configure(background='red')

    left = (int(screenWidth) - w) / 2
    top = (int(screenHeight) - h) / 2

    w_name.geometry("%dx%d+%d+%d" % (w, h, (left + x), (top + y)))

def input_hw(word):
    print("请输入分辨率的", str(word), ":")
    n = input()
    return n

def make_photo():
    make_window(root1, 20, 5, -25, 0)
    make_window(root2, 20, 5, 25, 0)
    make_window(root3, 5, 20, 0, -25)
    make_window(root4, 5, 20, 0, 25)

def left_event():
    root1.bind("<Button-1>", down_left())
    root2.bind("<Button-1>", down_left())
    root3.bind("<Button-1>", down_left())
    root4.bind("<Button-1>", down_left())

'''
def right_event():
    root1.bind("<Button-3>", down_right())
    root2.bind("<Button-3>", down_right())
    root3.bind("<Button-3>", down_right())
    root4.bind("<Button-3>", down_right())

def event():
    left_event()
    right_event()
'''

def on_key_press(event):
    # 阻止按键事件的进一步处理
    return "break"

screenWidth = input_hw("宽")     # 获取显示区域的宽度
screenHeight = input_hw("高")    # 获取显示区域的高度

root1 = tk.Tk()
root2 = tk.Tk()
root3 = tk.Tk()
root4 = tk.Tk()

#移除所有按键事件
root1.bind("<KeyPress>", on_key_press)
root2.bind("<KeyPress>", on_key_press)
root3.bind("<KeyPress>", on_key_press)
root4.bind("<KeyPress>", on_key_press)

while True:
    make_photo()
    #event()

    # 宽度x高度+x偏移+y偏移
    # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
    root1.mainloop()
    root2.mainloop()
    root3.mainloop()
    root4.mainloop()

