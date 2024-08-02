import win32gui
import pyautogui
import settings
import time

def enum_windows_callback(hwnd, window_titles):
    if win32gui.IsWindowVisible(hwnd):
        window_titles.append(win32gui.GetWindowText(hwnd))

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    pos_x, pos_y = pyautogui.position(x, y)
    color = pyautogui.pixel(pos_x, pos_y)
    return color

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

    print(f"Window '{window_title}' top-left corner coordinates:")
    print(f"x: {x}, y: {y}")
    print(get_color_at_position(x, y))

# タイトルを指定してウィンドウの座標を取得
while True:
    time.sleep(1)
    get_window_top_left_coordinates(settings.TITLE)
