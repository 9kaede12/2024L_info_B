# tkinterモジュールのインポート
import tkinter

# 選んだマップチップの番号を入れる変数
chip = 0
# 迷路のデータを入れるリスト
map_data = []
# 繰り返し処理
for i in range(9):
  # リストを初期化する
  map_data.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

# 迷路を書く関数
def draw_map():
  # いったん、全ての画像を削除
  cvs_bg.delete("BG")
  # 二重ループの
  for y in range(9):
    # 繰り返し処理
    for x in range(12):
      cvs_bg.create_image(60*x+30, 60*y+30, image=img[map_data[y][x]], tag="BG")

# 迷路のマップチップを置く関数
def set_map(e):
  # リストの添字xを求める
  x = int(e.x/60)
  # リストの添字yを求める
  y = int(e.y/60)
  # クリックした位置が迷路の範囲なら
  if 0 <= x and x <= 11 and 0 <= y and y <= 8:
    # リストにchipの値を入れ
    map_data[y][x] = chip
    # 迷路を描く変数
    draw_map()

# 洗濯用のマップチップを書く関数
def draw_chip():
  # 一旦、全ての画像を削除
  cvs_chip.delete("CHIP")
  # 繰り返し処理で
  for i in range(len(img)):
    cvs_chip.create_image(30, 30+i*60, image=img[i], tag="CHIP")
  cvs_chip.create_rectangle(4, 4+60*chip, 57, 57+60*chip, outline="red", width=3, tag="CHIP")

# マップチップを選ぶ関数
def select_chip(e):
  # chipをグローバル変数とする
  global chip
  # クリックしたy座標からチップの番号を計算
  y = int(e.y/60)
  # クリックした位置がマップチップなら
  if 0 <= y and y < len(img):
    # chipに選んだマップチップ番号を代入
    chip = y
    # 洗濯用のマップチップを描く関数
    draw_chip()

# データを出力する関数
def put_data():
  # キャンディを数えるための変数
  c = 0
  # テキスト入力欄の文字を全て削除
  text.delete("1.0", "end")
  # 二重ループの
  for y in range(9):
    # 繰り返し処理で
    for x in range(12):
      # 入力欄のデータを挿入
      text.insert("end", str(map_data[y][x])+",")
      # キャンディがあるなら
      if map_data[y][x] == 3:
        # キャンディカウントアップ
        c = c + 1
    # 改行コードを挿入
    text.insert("end", "\n")
  # キャンディの数を挿入
  text.insert("end", "candy = "+str(c))

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのサイズを指定
root.geometry("820x760")
# ウィンドウのタイトルを指定
root.title("マップエディタ")
cvs_bg = tkinter.Canvas(width=720, height=540, bg="white")
# キャンバスを配置
cvs_bg.place(x=10, y=10)
# クリックした時の関数を指定
cvs_bg.bind("<Button-1>", set_map)
# クリック＋ポインタ移動時の関数を指定
cvs_bg.bind("<B1-Motion>", set_map)
cvs_chip = tkinter.Canvas(width=60, height=540, bg="black")
# キャンバスを配置
cvs_chip.place(x=740, y=10)
# クリックした時の関数を指定
cvs_chip.bind("<Button-1>", select_chip)

# テキスト入力欄の部品を作る
text = tkinter.Text(width=40, height=14)
# テキスト入力欄を配置
text.place(x=10, y=560)
# ボタンの部品を作る
btn = tkinter.Button(text="データ出力", font=("Times New Roman", 16), fg="blue", command=put_data)
# ボタンを配置
btn.place(x=400, y=560)

# リストにマップチップの画像を読み込む
img = [
  tkinter.PhotoImage(file="info_B/L16/images/chip00.png"),
  tkinter.PhotoImage(file="info_B/L16/images/chip01.png"),
  tkinter.PhotoImage(file="info_B/L16/images/chip02.png"),
  tkinter.PhotoImage(file="info_B/L16/images/chip03.png"),
]
# 迷路を描画
draw_map()
# 選択用のマップチップを描画
draw_chip()
# ウィンドウを表示
root.mainloop()