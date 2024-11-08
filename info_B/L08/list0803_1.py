import tkinter

# キーコードを入れる変数
key = 0

# キーが押された時に実行される関数
def key_down(e):
	global key
	key = e.keycode

# リアルタイム処理を行う関数
def main_proc():
	label["text"] = key
	root.after(100, main_proc)

root = tkinter.Tk()
root.title("リアルタイムキー入力")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
main_proc()
root.mainloop()