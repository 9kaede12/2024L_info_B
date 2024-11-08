import tkinter

# キーコードを入れる変数
key = 0

# キーが押された時に実行する変数
def key_down(e):
    # グローバル変数として宣言
    global key
    # 押されたキーのコードを代入
    key = e.keycode
    print("KEY:" + str(key))

root = tkinter.Tk()
root.title("キーコードを取得")
# bind命令でキーを押した時に実行する関数を指定
root.bind("<KeyPress>", key_down)
# bind命令でキーを離した時に実行する関数を指定
# root.bind("<KeyRelease>", key_down)
# bind命令でマウスポインタを動かした時に実行する関数を指定
# root.bind("<Motion>", key_down)
# bind命令でマウスボタンをクリックした時に実行する関数を指定
# root.bind("<ButtonPress>", key_down)
# bind命令でマウスの左ボタンをクリックした時に実行する関数を指定
# root.bind("<Button-1>", key_down)
# bind命令でマウスの右ボタンをクリックした時に実行する関数を指定
# root.bind("<Button-3>", key_down)
root.mainloop()