import tkinter as tk
from PIL import ImageGrab
from pynput import mouse, keyboard

# 処理を制御するフラグ
processing_enabled = True

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    screenshot = ImageGrab.grab()  # スクリーンショットをその都度取得
    color = screenshot.getpixel((x, y))
    return color

def update_color_info():
    """カラー情報をメインウィンドウに表示"""
    if processing_enabled:
        x, y = mouse_controller.position
        color = get_color_at_position(x, y)
        r, g, b = color
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        
        # メインウィンドウのラベルに情報を表示
        info_label.config(text=f"マウス座標: ({x}, {y})\nRGBカラーコード: R={r}, G={g}, B={b}\n16進数カラーコード: {hex_color}")
        
        # 次の更新をスケジュールする
        root.after(10, update_color_info)

def on_key_press(key):
    """キー押下イベントを処理"""
    global processing_enabled
    try:
        if key == keyboard.Key.enter:
            processing_enabled = not processing_enabled
            if processing_enabled:
                update_color_info()  # 再開時に1回更新する
    except AttributeError:
        pass

def main():
    global root, info_label, mouse_controller
    
    # tkinterのルートウィンドウを作成
    root = tk.Tk()
    root.title("カラー情報")
    
    # メインウィンドウのサイズと位置を指定
    root.geometry("300x150+100+100")  # 初期位置は仮で設定
    
    # ウィンドウを常に最前面にする
    root.wm_attributes("-topmost", 1)
    
    # ラベルを作成して情報を表示
    info_label = tk.Label(root, text="マウスを動かして座標のカラーコードを取得します...", padx=10, pady=10)
    info_label.pack(expand=True, fill=tk.BOTH)
    
    # マウスリスナーを設定
    mouse_controller = mouse.Controller()
    
    # キーボードリスナーを設定
    key_listener = keyboard.Listener(on_press=on_key_press)
    key_listener.start()
    
    update_color_info()  # 最初の更新を開始する
    root.mainloop()
    key_listener.stop()

if __name__ == "__main__":
    main()
