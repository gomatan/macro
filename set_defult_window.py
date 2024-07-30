import pygetwindow as gw
import settings

# すべてのウィンドウのリストを取得
windows = gw.getWindowsWithTitle(settings.TITLE)  # 空文字列で全ウィンドウを取得

# 任意のウィンドウを選択
if windows:
    window = windows[0]  # 最初のウィンドウを選択
    print(f"現在のウィンドウ位置: {window.left}, {window.top}")

    # ウィンドウを (0, 0) に移動
    window.moveTo(0, 0)
    print(f"新しいウィンドウ位置: {window.left}, {window.top}")
else:
    print("ウィンドウが見つかりません")