# tkinterモジュールをインポートする
import tkinter
# フォントを指定する変数
FNT = ("Times New Roman", 30)

# クラスの宣言
class GameCharacter:
  # コンストラクタ
  def __init__(self, job, life, imgfile):
    # jobという属性に引数の値を代入
    self.job = job
    # lifeという属性に引数の値を代入
    self.life = life
    # img属性に画像を読み込む
    self.img = tkinter.PhotoImage(file=imgfile)

  # 画像と情報を表示するメソッド
  def draw(self):
    # 画像の描画
    canvas.create_image(200, 280, image=self.img)
    # 文字列の表示（jobの値）
    canvas.create_text(300, 400, text=self.job, font=FNT, fill="red")
    # 文字列の表示（lifeの値）
    canvas.create_text(300, 480, text=self.life, font=FNT, fill="blue")

# ウィンドウのオブジェクトを作る
root = tkinter.Tk()
# タイトルを指定
root.title("tkinterでオブジェクト指向プログラミング")
# キャンバスの部品を作る
canvas = tkinter.Canvas(root, width=400, height=560, bg="white")
# キャンバスを配置する
canvas.pack()

# キャラクターのオブジェクトを作る
character = GameCharacter("剣士", 200, "info_b/L13/images/swordsman.png")
character.draw()

# ウィンドウの表示
root.mainloop()