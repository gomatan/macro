import win32gui
import pyautogui
import settings
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def enum_windows_callback(hwnd, window_titles):
    if win32gui.IsWindowVisible(hwnd):
        window_titles.append(win32gui.GetWindowText(hwnd))

def get_color_at_position(x, y):
    #指定した座標のカラーコードを取得
    return pyautogui.pixel(x, y)

def get_window_top_left_coordinates(window_title):
    # ウィンドウハンドルを取得
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print("Window not found!")
        return

    # ウィンドウの座標を取得
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    return (x, y)


up_x, up_y = (376, 606) #上
down_x, down_y = (376, 586) #下
left_x, left_y = (380, 600) #左
right_x, right_y = (360, 600) #右
blue_button = (766, 604)
URDL = [(376, 606), (360, 600), (376, 586), (380, 600)]
x , y = get_window_top_left_coordinates(settings.TITLE)
w = 72

def press_key(index):
    if index == 0:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif index == 1:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif index == 2:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif index == 3:
        keyboard.press(Key.left)
        keyboard.release(Key.left)

def display_key(index):
    if index == 0:
        print('上')
    elif index == 1:
        print('右')
    elif index == 2:
        print('下')
    elif index == 3:
        print('左')
        
while True:
    if get_color_at_position(blue_button[0] + x, blue_button[1] + y) == (0, 131, 218):
        ww = 0
        yajirusi_arr = []
        for i in range(5):
            for index, arr in enumerate(URDL):
                pos_x = arr[0] + x + ww
                pos_y = arr[1] + y
                color = get_color_at_position(pos_x, pos_y)
                if color == (3, 183, 33):
                    yajirusi_arr.append(index)
            ww += w
        # print(yajirusi_arr)
        time.sleep(5)
        for index in yajirusi_arr:
            press_key(index)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        # while get_color_at_position(blue_button[0] + x, blue_button[1] + y) == (0, 131, 218):
        #     print('------------------------')
        #     for index, arr in enumerate(URDL):
        #         pos_x = arr[0] + x
        #         pos_y = arr[1] + y
        #         print(f'{get_color_at_position(pos_x, pos_y)}')
        #         color = get_color_at_position(pos_x, pos_y)
        #         if color == (3, 183, 33):
        #             press_key(index)
        #     time.sleep(1)
            


