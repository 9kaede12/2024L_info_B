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
  def draw(self, x, y):
    # 画像の描画
    canvas.create_image(x+200, y+280, image=self.img)
    # 文字列の表示（jobの値）
    canvas.create_text(x+300, y+400, text=self.job, font=FNT, fill="red")
    # 文字列の表示（lifeの値）
    canvas.create_text(x+300, y+480, text=self.life, font=FNT, fill="blue")

# ウィンドウのオブジェクトを作る
root = tkinter.Tk()
# タイトルを指定
root.title("tkinterでオブジェクト指向プログラミング")
# キャンバスの部品を作る
canvas = tkinter.Canvas(root, width=800, height=560, bg="white")
# キャンバスを配置する
canvas.pack()

# キャラクターのオブジェクトを作る
character = [
  # 剣士のオブジェクト
  GameCharacter("剣士", 200, "info_B/L13/images/swordsman.png"),
  # 忍者のオブジェクト
  GameCharacter("忍者", 160, "info_B/L13/images/ninja.png")
]
# 剣士オブジェクトのdraw()メソッドを実行
character[0].draw(0, 0)
# 忍者オブジェクトのdraw()メソッドを実行
character[1].draw(400, 0)

# ウィンドウの表示
root.mainloop()