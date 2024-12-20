# tkinterモジュールをインポートする
import tkinter

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのサイズを指定
root.geometry("400x200")
# ウィンドウのタイトルを指定
root.title("PythonでGUIを扱う")
# ラベルの部品を作る
label = tkinter.Label(root, text="ゲーム開発の一歩", font=("Times New Roman", 20))
# ラベルを配置
label.place(x=80, y=60)
# ウィンドウを表示
root.mainloop()