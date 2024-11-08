import tkinter
# カーソル座標
cursor_x = 0
cursor_y = 0
# マウスポインタ座標
mouse_x = 0
mouse_y = 0

# マウスポインタの座標取得関数
def mouse_movez(e):
  global mouse_x, mouse_y
  mouse_x = e.x
  mouse_y = e.y

# リアル処理タイム関数
def game_main():
  global cursor_x, cursor_y
  # マウスポインタが盤面上にあるか
  if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
    # マウスポインタの座標からカーソルの横と縦の位置を計算
    cursor_x = int((mouse_x - 24) / 72)
    cursor_y = int((mouse_y - 24) / 72)
  cvs.delete("CURSOR")
  cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
  root.after(100, game_main)

root = tkinter.Tk()
root.title("カーソルの表示")
root.resizable(False, False)
root.bind("<Motion>", mouse_movez)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="L09/images/neko_bg.png")
cursor = tkinter.PhotoImage(file="L09/images/neko_cursor.png")
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()