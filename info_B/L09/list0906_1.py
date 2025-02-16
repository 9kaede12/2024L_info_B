import tkinter
import random

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_movez(e):
  global mouse_x, mouse_y
  mouse_x = e.x
  mouse_y = e.y

def mouse_press(e):
  global mouse_c
  mouse_c = 1

# マス目を管理する二次元リスト
neko = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]

# 猫を表示する関数
def draw_neko():
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

# 猫を落下させる関数
def drop_neko():
  for y in range(8, -1, -1):
    for x in range(8):
      # 猫のいるマスの下が空白なら
      if neko[y][x] != 0 and neko[y+1][x] == 0:
        # 空白に猫を落とす
        neko[y+1][x] = neko[y][x]
        # 元のマスを空白にする
        neko[y][x] = 0

# メインの関数
def game_main():
  global cursor_x, cursor_y, mouse_c
  drop_neko()
  if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
    # マウスポインタの座標からカーソルの横と縦の位置を計算
    cursor_x = int((mouse_x - 24) / 72)
    cursor_y = int((mouse_y - 24) / 72)
    if mouse_c == 1:
      mouse_c = 0
      neko[cursor_y][cursor_x] = random.randint(1, 6)
  cvs.delete("CURSOR")
  cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
  cvs.delete("NEKO")
  draw_neko()
  root.after(100, game_main)

root = tkinter.Tk()
root.title("クリックをして猫を置く")
root.resizable(False, False)
root.bind("<Motion>", mouse_movez)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

# 背景画像
bg = tkinter.PhotoImage(file="L09/images/neko_bg.png")
cursor = tkinter.PhotoImage(file="L09/images/neko_cursor.png")
# リストで複数の猫画像を管理
img_neko =[
  None,
  tkinter.PhotoImage(file="L09/images/neko1.png"),
  tkinter.PhotoImage(file="L09/images/neko2.png"),
  tkinter.PhotoImage(file="L09/images/neko3.png"),
  tkinter.PhotoImage(file="L09/images/neko4.png"),
  tkinter.PhotoImage(file="L09/images/neko5.png"),
  tkinter.PhotoImage(file="L09/images/neko6.png"),
  tkinter.PhotoImage(file="L09/images/neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()