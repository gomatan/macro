import win32gui
import settings

def enum_windows_callback(hwnd, window_titles):
    if win32gui.IsWindowVisible(hwnd):
        window_titles.append(win32gui.GetWindowText(hwnd))

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


# タイトルを指定してウィンドウの座標を取得

get_window_top_left_coordinates(settings.TITLE)
