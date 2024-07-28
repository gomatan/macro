from PIL import ImageGrab
from pynput import mouse

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    # スクリーンショットを取得
    screenshot = ImageGrab.grab()
    
    # クリック位置のピクセルカラーを取得
    color = screenshot.getpixel((x, y))

    # RGBカラーを16進数に変換
    hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])

    return hex_color

def on_click(x, y, button, pressed):
    """マウスクリックイベントを処理"""
    if pressed:
        # クリックした座標のカラーコードを取得
        color = get_color_at_position(x, y)
        
        print(f"クリックした座標: ({x}, {y})")
        print(f"カラーコード: {color}")
        
        # クリック後にプログラムを終了
        return False

def main():
    print("クリックして座標のカラーコードを取得します...")
    
    # マウスイベントリスナーを設定
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()