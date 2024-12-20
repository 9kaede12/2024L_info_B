# tkinterモジュールをインポートする
import tkinter
# timeモジュールをインポートする
import time
# フォントを指定する変数
FNT = ("Times New Roman", 24)

# クラスの宣言
class GameCharacter:
  # コンストラクタ
  def __init__(self, name, life, x, y, imgfile, tagname):
    # name属性に引数の値を代入
    self.name = name
    # life属性に引数の値を代入
    self.life = life
    # lmax属性に引数の値を代入
    self.lmax = life
    # x属性に引数の値を代入
    self.x = x
    # y属性に引数の値を代入
    self.y = y
    # img属性に画像を読み込む
    self.img = tkinter.PhotoImage(file=imgfile)
    # tagname属性に引数の値を代入
    self.tagname = tagname

  # 画像と情報を表示するメソッド
  def draw(self):
    # 変数xに表示位置（x座標）を代入
    x = self.x
    # 変数yに表示位置（y座標）を代入
    y = self.y
    # 画像の描画
    canvas.create_image(x, y, image=self.img, tag=self.tagname)
    # 文字列の表示（jobの値）
    canvas.create_text(x, y+120, text=self.name, font=FNT, fill="red", tag=self.tagname)
    # 文字列の表示（lifeの値）
    canvas.create_text(x, y+200, text="life{}/{}".format(self.life, self.lmax), font=FNT, fill="lime", tag=self.tagname)

  # 攻撃処理を行うメソッド
  def attack(self):
    # 画像を動かす向き
    dir = 1
    # 右側のキャラは
    if self.x >= 400:
      # 動かす向きを左側とする
      dir = -1
    # 攻撃動作（横に動かす）繰り返しで
    for i in range(5):
      # キャラを表示するメソッド
      canvas.coords(self.tagname, self.x+i*10*dir, self.y)
      # キャンバスを更新
      canvas.update()
      # 0.1秒待つ
      time.sleep(0.1)
    # 画像を元の位置に移動
    canvas.coords(self.tagname, self.x, self.y)

  # ダメージを受ける処理を行うメソッド
  def damage(self):
    # ダメージ（画像の点滅）繰り返しで
    for i in range(5):
      # キャラを表示するメソッド
      self.draw()
      # キャンバスを更新
      canvas.update()
      # 0.1秒待つ
      time.sleep(0.1)
      # 画像を削除（一旦消す）
      canvas.delete(self.tagname)
      # キャンバスを更新
      canvas.update()
      # 0.1秒待つ
      time.sleep(0.1)
    # ライフを30減らす
    self.life = self.life - 30
    # ライフが0より大きければ
    if self.life > 0:
      # キャラを表示する
      self.draw()
    # そうでなければ
    else:
      # 倒れたとターミナルまたはシェルウィンドウ画面に表示する
      print(self.name+"は倒れた...")

# 左側のボタンをクリックした時の関数
def click_left():
  # 剣士の攻撃処理のメソッドを実行
  character[0].attack()
  # 忍者のダメージ処理のメソッドを実行
  character[1].damage()

# 右側のボタンをクリックした時の関数
def click_right():
  # 忍者の攻撃処理のメソッドを実行
  character[1].attack()
  # 剣士のダメージ処理のメソッドを実行
  character[0].damage()

# ウィンドウのオブジェクトを作る
root = tkinter.Tk()
# タイトルを指定
root.title("オブジェクト指向でバトル")
# キャンバスの部品を作る
canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
# キャンバスを配置する
canvas.pack()

# 左側のボタンを作る
btn_left = tkinter.Button(text="攻撃→", command=click_left)
# 配置する
btn_left.place(x=160, y=560)
# 右側のボタンを作る
btn_right = tkinter.Button(text="←攻撃", command=click_right)
# 配置する
btn_right.place(x=560, y=560)

# リストでオブジェクトを作る
character = [
  # 剣士のオブジェクト
  GameCharacter("暁の剣士「ガイア」", 200, 200, 280, "info_B/L13/images/swordsman.png", "LC"),
  # 忍者のオブジェクト
  GameCharacter("闇の忍者「半蔵」", 160, 600, 280, "info_B/L13/images/ninja.png", "RC")
]
# 剣士オブジェクトのdraw()メソッドを実行
character[0].draw()
# 忍者オブジェクトのdraw()メソッドを実行
character[1].draw()

# ウィンドウの表示
root.mainloop()