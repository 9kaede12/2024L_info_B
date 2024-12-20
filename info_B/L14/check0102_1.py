# tkinterモジュールをインポートする
import tkinter
# datetimeモジュールをインポートする
import datetime

# 関数の定義
def time_now():
  # 変数dに現在の日時を代入
  d = datetime.datetime.now()
  # 変数tに時アワー、分ミニッツ、秒セコンドを代入
  t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second)
  # ラベルの文字列を変更
  label["text"] = t
  # １秒後に再びこの関数を実行
  root.after(1000, time_now)

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのサイズを指定
root.geometry("400x100")
# ウィンドウのタイトルを指定
root.title("簡易時計")
# ラベルの部品を作る
label = tkinter.Label(font=("Times New Roman", 60))
# ラベルを配置
label.pack()
# time_now()関数を実行
time_now()
# ウィンドウを表示
root.mainloop()