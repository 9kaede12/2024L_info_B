import tkinter
import random

def click_btn1():
	label1["text"]=random.choice(["大吉", "中吉", "小吉", "吉", " 凶 ", "大凶"])
	label1.update()

def click_btn2():
	label2["text"]=random.choice(["ブルー", "レッド", "イエロー", "グリーン", "ピンク", "ブラック", "ホワイト"])
	# 色名に対応する実際の色を設定
	color_map = {
		"ブルー": "blue",
		"レッド": "red",
		"イエロー": "yellow",
		"グリーン": "green",
		"ピンク": "pink",
		"ブラック": "black",
		"ホワイト": "white",
	}
	label2["bg"] = color_map[label2["text"]]
	# 文字色を調整（背景が黒か青の場合は白文字、それ以外は黒文字）
	label2["fg"] = "white" if label2["text"] == "ブラック" or label2["text"] == "ブルー" else "black"

	label2.update()

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="info_B/L06/images/miko.png")
canvas.create_image(400, 300, image=gazou)

label1 = tkinter.Label(root, text="？？", font=("Times New Roman", 40), bg="black")
label2 = tkinter.Label(root, text="？？", font=("Times New Roman", 40), bg="black")
label1.place(x=200, y=80)
label2.place(x=200, y=400)
button1 = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 20), command=click_btn1, fg="black")
button1.place(x=450, y=80)
button2 = tkinter.Button(root, text="ラッキーカラー", font=("Times New Roman", 20), command=click_btn2, fg="red")
button2.place(x=450, y=400)
root.mainloop()