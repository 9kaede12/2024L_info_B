import tkinter

# マス目を管理する二次元リスト
neko = [
  [1, 0, 0, 0, 0, 0, 7, 7],
  [0, 2, 0, 0, 0, 0, 7, 7],
  [0, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 0, 4, 0, 0, 0, 0],
  [0, 0, 0, 0, 5, 0, 0, 0],
  [0, 0, 0, 0, 0, 6, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 2, 3, 4, 5, 6]
]

# 猫を表示する関数
def draw_neko():
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]])

root = tkinter.Tk()
root.title("二次元リストでマスを管理する")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

# 背景画像
bg = tkinter.PhotoImage(file="L09/images/neko_bg.png")
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
draw_neko()
root.mainloop()