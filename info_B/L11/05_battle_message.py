import pygame
import sys

# 色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# 先頭の背景画像を読み込む
imgBtlBG = pygame.image.load("info_B/L11/images/btlbg.png")
# 敵の画像を読み込むための変数を用意この時点ではなし
imgEnemy = pygame.image.load("info_B/L11/images/enemy1.png")
# 敵キャラクター表示位置のx座標
emy_x = 440-imgEnemy.get_width()/2
# 敵キャラクター表示位置のy座標
emy_y = 560-imgEnemy.get_height()

# 先頭メッセージを入れるリスト
message = [""]*10
# メッセージをからにする関数
def init_massege():
  for i in range(10):
    message[i] = ""

# メッセージをセットする関数
def set_message(msg):
  for i in range(10):
    # 文字列がセットされていないリストがあれば
    if message[i] == "":
      message[i] = msg
      return
  for i in range(9):
    message[i] = message[i+1]
  message[9] = msg

# 影付きの文字列を書く関数
def draw_text(bg, txt, x, y, fnt, col):
  sur = fnt.render(txt, True, BLACK)
  bg.blit(sur, [x+1, y+2])
  sur = fnt.render(txt, True, col)
  bg.blit(sur, [x, y])

# 戦闘画面を描画する関数
def draw_battle(bg, fnt):
  bg.blit(imgBtlBG, [0, 0])
  bg.blit(imgEnemy, [emy_x, emy_y])
  for i in range(10):
    draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)

# メイン関数
def main():
  # モジュールの初期化
  pygame.init()
  # タイトルを設定
  pygame.display.set_caption("戦闘中のメッセージ")
  # 描画画面の初期化
  screen = pygame.display.set_mode((880, 720))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # フォントオブジェクトの作成
  font = pygame.font.Font(None, 40)

  # 戦闘に入る準備をする関数を呼ぶ
  init_massege()

  # 無限ループ
  while True:
    # pygameイベントを繰り返しで処理
    for event in pygame.event.get():
      # 閉じるボタンが押されたら
      if event.type == pygame.QUIT:
        # pygameの初期化を解除
        pygame.quit()
        # プログラムを終了
        sys.exit()
      # キーを押すイベントが発生したら
      if event.type == pygame.KEYDOWN:
        set_message("KEYDOWN "+str(event.key))

    # 先頭画面を描画
    draw_battle(screen, font)
    # 画面を更新
    pygame.display.update()
    # フレームレートを５秒に設定
    clock.tick(5)

if __name__ == '__main__':
  main()