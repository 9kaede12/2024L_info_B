# tkinterモジュールのインポート
import tkinter

# フォントの定義（小さなサイズ）
fnt1 = ("Times New Roman", 20)
# フォントの定義（大きなサイズ）
fnt2 = ("Times New Roman", 40)
# インデックス用の変数
index = 0
# タイマー用の変数
timer = 0

# キーの値を代入する変数
key = ""
# キーが押された時に実行する関数
def key_down(e):
  # グローバル変数とする
  global key
  # キーシンボルの値を代入
  key = e.keysym

# メイン処理を行う関数
def main():
  # グローバル変数とする
  global index, timer
  # 一旦、indexとtimerの表示を消す
  canvas.delete("STATUS")
  # timerの値を１ずつ増やす
  timer = timer + 1
  # indexの値を表示
  canvas.create_text(200, 30, text="index "+str(index), fill="white", font=fnt1, tag="STATUS")
  # timerの値を表示
  canvas.create_text(400, 30, text="timer "+str(timer), fill="cyan", font=fnt1, tag="STATUS")

  # インデックス０の処理「タイトル画面」
  if index == 0:
    # timerが１なら
    if timer == 1:
      # タイトルの文字を表示
      canvas.create_text(300, 150, text="タイトル", fill="white", font=fnt2, tag="TITLE")
      # Press[SPACE]Keyと表示
      canvas.create_text(300, 300, text="Press[SPACE]Key", fill="lime", font=fnt2, tag="TITLE")
    # スペースキーが押されたら
    if key == "space":
      # タイトルの文字を消し
      canvas.delete("TITLE")
      # キャンバスを青で塗り潰す
      canvas.create_rectangle(0, 0, 600, 400, fill="blue", tag="GAME")
      # ゲーム中の文字を表示
      canvas.create_text(300, 150, text="ゲーム中", fill="white", font=fnt2, tag="GAME")
      # [E]終了の文字を表示
      canvas.create_text(300, 300, text="[E]終了", fill="yellow",font=fnt1, tag="GAME")
      # indexの値を１にする
      index = 1
      # timerの値を０にする
      timer = 0

  # インデックス１の処理「ゲーム中」
  if index == 1:
    # Eキーが押されたら
    if key == "e":
      # ゲーム中という文字を消し
      canvas.delete("GAME")
      # キャンバスを栗色で塗り潰す
      canvas.create_rectangle(0, 0, 600, 400, fill="maroon", tag="OVER")
      # GAME OVERの文字を表示
      canvas.create_text(300, 150, text="GAME OVER", fill="red",font=fnt2, tag="OVER")
      # indexの値を２にする
      index = 2
      # timerの値を０にする
      timer = 0

  # インデックス２の処理「ゲームオーバー画面」
  if index == 2:
    # timerも値が３０になったら
    if timer == 30:
      # ゲームオーバーの文字を消し
      canvas.delete("OVER")
      # indexの値を０にする
      index = 0
      # timerの値を０にする
      timer = 0

  # １００m秒後に再びmain()関数を実行
  root.after(100, main)

# ウィンドウの部品を作る
root = tkinter.Tk()
# ウィンドウのタイトルを指定
root.title("インデックスとタイマー")
# キーを押した時に実行する関数をして
root.bind("<KeyPress>", key_down)
# キャンバスの部品を作る
canvas = tkinter.Canvas(width=600, height=400, bg="black")
# キャンパスをウィンドウに配置
canvas.pack()
# メイン処理を実行
main()
# ウィンドウを表示
root.mainloop()