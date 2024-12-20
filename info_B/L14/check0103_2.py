# tkinterモジュールをインポートする
import tkinter

# スクロール位置を管理する変数
x = 0
# 関数の定義
def scroll_bg():
  # xをグローバル変数として扱う
  global x
  # xの値を１増やす
  x = x + 1
  # xが４８０になったら
  if x == 480:
    # xを０にする
    x = 0
  # 一旦、背景画像を削除する
  canvas.delete("BG")
  # 背景画像を描画（左側）
  canvas.create_image(x-240, 150, image=img_bg, tag="BG")
  # 背景画像を描画（右側）
  canvas.create_image(x+240, 150, image=img_bg, tag="BG")
  # ５０粍秒後に再びこの関数を実行
  root.after(50, scroll_bg)

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのタイトルを指定
root.title("画面のスクロール")
# キャンバスの部品を作る
canvas = tkinter.Canvas(width=480, height=300)
# キャンバスを配置
canvas.pack()
# 変数img_bgに画像を読み込む
img_bg = tkinter.PhotoImage(file="info_B/L14/images/park.png")
# 画像をスクロールする関数を実行
scroll_bg()
# ウィンドウを表示
root.mainloop()