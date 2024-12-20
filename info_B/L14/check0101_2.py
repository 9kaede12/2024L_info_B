# tkinterモジュールをインポートする
import tkinter

# 関数の定義
def key_down(e):
  # 変数key_cにキーコードの値を代入
  key_c = e.keycode
  # ラベル１にその値を表示
  label1["text"] = "keycode "+str(key_c)
  # 変数key_sにキーシンボルの値を代入
  key_s = e.keysym
  # ラベル２にその値を表示
  label2["text"] = "keysym "+key_s

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのサイズを指定
root.geometry("400x200")
# ウィンドウのタイトルを指定
root.title("キー入力")
# キーが押された時に実行する関数を指定
root.bind("<KeyPress>", key_down)
# フォントを定義
fnt = ("Times New Roman", 30)
# ラベル１の部品を作る
label1 = tkinter.Label(text="keycode", font=fnt)
# ラベル１を配置
label1.place(x=0, y=0)
# ラベル２の部品を作る
label2 = tkinter.Label(text="keysym", font=fnt)
# ラベル２を配置
label2.place(x=0, y=80)
# ウィンドウを表示
root.mainloop()