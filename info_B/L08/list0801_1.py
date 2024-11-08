import tkinter

# 時間をカウントする変数
tmr = 0

# リアルタイム処理を行う関数
def count_up():
    # グローバル変数として宣言
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    # 1秒後に再度自分自身を実行
    root.after(1000, count_up)

root = tkinter.Tk()
label = tkinter.Label(font=("TImes New Roman", 80))
label.pack()
# root.after(1000, count_up)
count_up()
root.mainloop()