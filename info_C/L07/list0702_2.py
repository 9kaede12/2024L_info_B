import tkinter

def click_btn():
    txt = text.get("1.0", "end-1c")
    text.insert(tkinter.END, txt)

root = tkinter.Tk()
root.title("複数行のテキスト入力")
root.geometry("400x200")
button = tkinter.Button(text="メッセージ", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()