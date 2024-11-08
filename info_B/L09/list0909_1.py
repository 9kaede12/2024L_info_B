import tkinter
import random

index = 0
timer = 0
score = 0
tsugi = 0

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
neko = []
# 判定用の二次元リスト
check = []
# リストを初期化
for i in range(10):
  neko.append([0, 0, 0, 0, 0, 0, 0, 0])
  check.append([0, 0, 0, 0, 0, 0, 0, 0])

# 猫を表示する関数
def draw_neko():
  cvs.delete("NEKO")
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

# 猫が縦・横・斜め出揃ったか判定する関数
def check_neko():
  for y in range(10):
    for x in range(8):
      # 判定用リストに盤面をコピー
      check[y][x] = neko[y][x]

  for y in range(1, 9):
    for x in range(8):
      if check[y][x] > 0:
        # 上下判定
        if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
          neko[y - 1][x] = 7
          neko[y][x] = 7
          neko[y + 1][x] = 7

  for y in range(10):
    for x in range(1, 7):
      if neko[y][x] > 0:
        # 左右判定
        if neko[y][x - 1] == neko[y][x] and neko[y][x + 1] == neko[y][x]:
          neko[y][x - 1] = 7
          neko[y][x] = 7
          neko[y][x + 1] = 7

  for y in range(1, 9):
    for x in range(1, 7):
      if neko[y][x] > 0:
        # 斜め判定（左上と右下）
        if neko[y - 1][x - 1] == neko[y][x] and neko[y + 1][x + 1] == neko[y][x]:
          neko[y - 1][x - 1] = 7
          neko[y][x] = 7
          neko[y + 1][x + 1] = 7
        # 斜め判定（左下と右上）
        if neko[y + 1][x - 1] == neko[y][x] and neko[y - 1][x + 1] == neko[y][x]:
          neko[y + 1][x - 1] = 7
          neko[y][x] = 7
          neko[y - 1][x + 1] = 7

def sweep_neko():
  num = 0
  for y in range(10):
    for x in range(8):
      if neko[y][x] == 7:
        neko[y][x] = 0
        num = num + 1
  return num

def drop_neko():
  flg = False
  for y in range(8, -1, -1):
    for x in range(8):
      if neko[y][x] != 0 and neko[y + 1][x] == 0:
        neko[y + 1][x] = neko[y][x]
        neko[y][x] = 0
        flg = True
  return flg

def over_neko():
  for x in range(8):
    if neko[0][x] > 0:
      return True
  return False

def set_neko():
  for x in range(8):
    neko[0][x] = random.randint(0, 6)

def draw_txt(txt, x, y, siz, col, tg):
  fnt = ("Times New Roman", siz, "bold")
  cvs.create_text(x + 2, y + 2, text = txt, fill = "black", font = fnt, tag = tg)
  cvs.create_text(x, y, text = txt, fill = col, font = fnt, tag = tg)

# メインの関数
def game_main():
  global index, timer, score, tsugi
  global cursor_x, cursor_y, mouse_c
  if index == 0:
    draw_txt("ねこねこ", 312, 240, 100, "violet", "TITLE")
    draw_txt("Click to start", 312, 560 , 50, "orange", "TITLE")
    index = 1
    mouse_c = 0
  elif index == 1:
    if mouse_c == 1:
      for y in range(10):
        for x in range(8):
          neko[y][x] = 0
      mouse_c = 0
      score = 0
      tsugi = 0
      cursor_x = 0
      cursor_y = 0
      set_neko()
      draw_neko()
      cvs.delete("TITLE")
      index = 2
  elif index == 2:
    if drop_neko() == False:
      index = 3
    draw_neko()
  elif index == 3:
    check_neko()
    draw_neko()
    index = 4
  elif index == 4:
    sc = sweep_neko()
    score = score + sc * 10
    if sc > 0:
      index = 2
    else:
      if over_neko() == False:
        tsugi = random.randint(1, 6)
        index = 5
      else:
        index = 6
        timer = 0
    draw_neko()
  elif index == 5:
    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
      # マウスポインタの座標からカーソルの横と縦の位置を計算
      cursor_x = int((mouse_x - 24) / 72)
      cursor_y = int((mouse_y - 24) / 72)
      if mouse_c == 1:
        mouse_c = 0
        set_neko()
        neko[cursor_y][cursor_x] = tsugi
        tsugi = 0
        index = 2
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
  elif index == 6:
    timer = timer + 1
    if timer == 1:
      draw_txt("GAME OVER", 312, 248, 60, "red", "OVER")
    if timer == 50:
      cvs.delete("OVER")
      index = 0
  cvs.delete("INFO")
  draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
  if tsugi > 0:
    cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
  root.after(100, game_main)

root = tkinter.Tk()
root.title("落ち物パズル「ねこねこ」")
root.resizable(False, False)
root.bind("<Motion>", mouse_movez)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

# 背景画像
bg = tkinter.PhotoImage(file="info_B/L09/images/neko_bg.png")
cursor = tkinter.PhotoImage(file="info_B/L09/images/neko_cursor.png")
# リストで複数の猫画像を管理
img_neko =[
  None,
  tkinter.PhotoImage(file="info_B/L09/images/neko1.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko2.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko3.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko4.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko5.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko6.png"),
  tkinter.PhotoImage(file="info_B/L09/images/neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()