# tkinterモジュールをインポートする
import tkinter

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのタイトルを指定
root.title("Canvasに画像を描画する")
# キャンバスの部品を作る
canvas = tkinter.Canvas(width=480, height=300)
# キャンパスを配置
canvas.pack()
# 変数img_bgに画像を表示
img_gb = tkinter.PhotoImage(file="info_B/L14/images/park.png")
# キャンバスに画像を表示
canvas.create_image(240, 150, image=img_gb)
# ウィンドウを表示
root.mainloop()