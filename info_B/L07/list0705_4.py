import tkinter

# 診断結果の出力リスト
KEKKA = [
    "前世が猫だった可能性は極めて薄いです。",
    "至って普通の人間です。",
    "特別、おかしなところはありません。",
    "やや、猫っぽいところがあります。",
    "猫に近い性格のようです。",
    "猫にかなり近い性格です。",
    "前世は猫だったかもしれません。",
    "見た目は人間、中身は猫の可能性があります。"
]

def click_btn(): # ボタンを押した時の関数
    pts = 0 # チェックされたチェックボタンの数を格納する
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    nekodo = int(100*pts/7) # ネコ度の計算、整数表示
    text.delete("1.0", tkinter.END) # 入力欄を初期化
    # 診断結果を出力（ベタで表示）
    text.insert("1.0", "＜診断結果＞\nあなたのネコ度は" + str(nekodo) + "%です。\n" + KEKKA[pts])

root = tkinter.Tk()
root.title("ネコ度診断アプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="L07/images/sumire.png")
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None]*7 # BooleanVarオブジェクト用のリスト
cbtn = [None]*7 # チェックボックス用のリスト
ITEM = ["高いところが好き","ボールを見ると転がしたくなる",
        "びっくりすると髪の毛が逆立つ", "ネズミの玩具が気になる",
        "匂いに敏感", "魚の骨をしゃぶりたくなる", "夜、元気になる"]
for i in range(7): # ITEMの要素分繰り返す
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe", fg="black")
    cbtn[i].place(x=400, y=160+40*i)
root.mainloop()