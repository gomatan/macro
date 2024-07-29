from PIL import ImageGrab
from pynput import mouse

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    # スクリーンショットを取得
    screenshot = ImageGrab.grab()
    
    # クリック位置のピクセルカラーを取得
    color = screenshot.getpixel((x, y))

    return color

def on_move(x, y):
    """マウス移動イベントを処理"""
    # マウスが移動するたびに座標のカラーコードを取得
    color = get_color_at_position(x, y)
    
    # RGBカラーの各要素を取得
    r, g, b = color
    
    # カラーコードを16進数に変換
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    print(f"マウス座標: ({x}, {y})")
    print(f"RGBカラーコード: R={r}, G={g}, B={b}")
    print(f"16進数カラーコード: {hex_color}")

def on_click(x, y, button, pressed):
    """マウスクリックイベントを処理"""
    if not pressed:
        # クリックがリリースされたときにリスナーを停止
        return False

def main():
    print("マウスを動かして座標のカラーコードを取得します...")
    
    # マウスイベントリスナーを設定
    with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
