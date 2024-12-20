# tkinterモジュールをインポートする
import tkinter

# スクロール位置を管理する変数
x = 0
# 犬のアニメーション用の変数
ani = 0
# 関数の定義
def animation():
  # グローバル変数として扱う
  global x, ani
  # xの値を１増やす
  x = x + 4
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
  # aniの値を０〜３の範囲で変化させる
  ani = (ani+1)%4
  # 犬の画像をを描画
  canvas.create_image(240, 200, image=img_dog[ani], tag="BG")
  # ５０粍秒後に再びこの関数を実行
  root.after(200, animation)

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのタイトルを指定
root.title("アニメーション")
# キャンバスの部品を作る
canvas = tkinter.Canvas(width=480, height=300)
# キャンバスを配置
canvas.pack()
# 変数img_bgに画像を読み込む
img_bg = tkinter.PhotoImage(file="info_B/L14/images/park.png")
# アニメーション用の画像４枚
img_dog = [
  tkinter.PhotoImage(file="info_B/L14/images/dog0.png"),
  tkinter.PhotoImage(file="info_B/L14/images/dog1.png"),
  tkinter.PhotoImage(file="info_B/L14/images/dog2.png"),
  tkinter.PhotoImage(file="info_B/L14/images/dog3.png")
]
# アニメーションを表示する関数を実行
animation()
# ウィンドウを表示
root.mainloop()