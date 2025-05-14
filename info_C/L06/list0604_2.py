import tkinter
root = tkinter.Tk()
root.title("初めての画像表示")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="info_C/L06/images/iroha.png")
canvas.create_image(200, 300, image=gazou)
# canvas.create_image(0, 0, image=gazou)
root.mainloop()