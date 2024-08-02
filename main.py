import tkinter as tk
from PIL import ImageGrab
from pynput import mouse

# 処理を制御するフラグ
processing_enabled = True

def get_color_at_position(x, y):
    """指定した座標のカラーコードを取得"""
    screenshot = ImageGrab.grab()  # スクリーンショットをその都度取得
    color = screenshot.getpixel((x, y))
    return color

def update_color_info(x, y):
    """カラー情報をメインウィンドウに表示"""
    if processing_enabled:
        x, y = mouse_controller.position
        color = get_color_at_position(x, y)
        r, g, b = color
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        
        # メインウィンドウのラベルに情報を表示
        info_label.config(text=f"マウス座標: ({x}, {y})\nRGBカラーコード: R={r}, G={g}, B={b}\n16進数カラーコード: {hex_color}")
        
        # 色サンプルを更新
        color_sample_canvas.create_rectangle(0, 0, 50, 50, fill=hex_color, outline=hex_color)
        
        # 次の更新をスケジュールする
        root.after(10, update_color_info)

def toggle_processing(event):
    """Enterキー押下イベントを処理"""
    global processing_enabled
    processing_enabled = not processing_enabled
    if processing_enabled:
        update_color_info()  # 再開時に1回更新する

def main():
    global root, info_label, color_sample_canvas, mouse_controller
    
    # tkinterのルートウィンドウを作成
    root = tk.Tk()
    root.title("カラー情報")
    
    # メインウィンドウのサイズと位置を指定
    root.geometry("300x200+100+100")  # 初期位置は仮で設定
    
    # ラベルを作成して情報を表示
    info_label = tk.Label(root, text="マウスを動かして座標のカラーコードを取得します...", padx=10, pady=10)
    info_label.pack(expand=True, fill=tk.BOTH)
    
    # 色サンプルを表示するキャンバスを作成
    color_sample_canvas = tk.Canvas(root, width=50, height=50)
    color_sample_canvas.pack(pady=10)
    
    # マウスリスナーを設定
    mouse_controller = mouse.Controller()
    
    # tkinterウィンドウにキーイベントリスナーを設定
    root.bind('<Return>', toggle_processing)
    
    update_color_info()  # 最初の更新を開始する
    root.mainloop()

if __name__ == "__main__":
    main()