import tkinter as tk
from PIL import ImageGrab
from pynput import mouse
import time

# スクリーンショットを取得する間隔（秒）
screenshot = ImageGrab.grab()

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    
    color = screenshot.getpixel((x, y))
    return color

def update_color_info(x, y):
    """カラー情報をメインウィンドウに表示"""
    color = get_color_at_position(x, y)
    r, g, b = color
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    # メインウィンドウのラベルに情報を表示
    info_label.config(text=f"マウス座標: ({x}, {y})\nRGBカラーコード: R={r}, G={g}, B={b}\n16進数カラーコード: {hex_color}")

def on_move(x, y):
    """マウス移動イベントを処理"""
    
    update_color_info(x, y)
        
def on_click(x, y, button, pressed):
    """マウスクリックイベントを処理"""
    if not pressed:
        return False

def main():
    global info_label
    
    # tkinterのルートウィンドウを作成
    root = tk.Tk()
    root.title("カラー情報")
    
    # メインウィンドウのサイズと位置を指定
    root.geometry("300x150+100+100")  # サイズと位置 (幅x高さ+X座標+Y座標)
    
    # ラベルを作成して情報を表示
    info_label = tk.Label(root, text="マウスを動かして座標のカラーコードを取得します...", padx=10, pady=10)
    info_label.pack(expand=True, fill=tk.BOTH)
    
    # マウスリスナーを設定
    with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
        root.mainloop()

if __name__ == "__main__":
    main()