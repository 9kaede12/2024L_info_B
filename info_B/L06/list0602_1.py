import tkinter
root = tkinter.Tk()
root.title("初めてのウィンドウ")
root.geometry("800x600")
label = tkinter.Label(root, text="ラベルの文字列", font=("System", 24))
label.place(x=200, y=100)
# label.place(x=0, y=0)
root.mainloop()