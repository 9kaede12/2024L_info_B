import tkinter

def click_btn():
    text.insert(tkinter.END, "モンスターが現れた！")

root = tkinter.Tk()
root.title("複数行のテキスト入力欄")
root.geometry("400x200")
button = tkinter.Button(text="メッセージ", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
# text.place(x=20, y=50, width=360, height=120)
root.mainloop()