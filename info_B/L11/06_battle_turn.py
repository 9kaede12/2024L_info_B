import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# 先頭の背景画像を読み込む
imgBtlBG = pygame.image.load("info_B/L11/images/btlbg.png")
# 攻撃エフェクトの画像を読み込む
imgEffect = pygame.image.load("info_B/L11/images/effect_a.png")
# 敵の画像を読み込むための変数を用意この時点ではなし
imgEnemy = pygame.image.load("info_B/L11/images/enemy1.png")
# 敵キャラクター表示位置のx座標
emy_x = 440-imgEnemy.get_width()/2
# 敵キャラクター表示位置のy座標
emy_y = 560-imgEnemy.get_height()
# 敵キャラを手前に移動するための変数
emy_Step = 0
# 敵キャラを点滅されるための変数
emy_blink = 0
# 画面を揺らすための変数
dmg_eff = 0
# 戦闘コマンド
COMMAND = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]

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
  global emy_blink, dmg_eff
  bx = 0
  by = 0
  if dmg_eff > 0:
    dmg_eff = dmg_eff - 1
    bx = random.randint(-20, 20)
    by = random.randint(-10, 10)
  bg.blit(imgBtlBG, [bx, by])
  if emy_blink%2 == 0:
    bg.blit(imgEnemy, [emy_x, emy_y+emy_Step])
  if emy_blink > 0:
    emy_blink = emy_blink - 1
  for i in range(10):
    draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)

def battle_command(bg, fnt):
  for i in range(4):
    draw_text(bg, COMMAND[i], 20, 360+60*i, fnt, WHITE)

# メイン関数
def main():
  global emy_Step, emy_blink, dmg_eff
  idx = 10
  tmr = 0

  # モジュールの初期化
  pygame.init()
  # タイトルを設定
  pygame.display.set_caption("ターン制の処理")
  # 描画画面の初期化
  screen = pygame.display.set_mode((880, 720))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # フォントオブジェクトの作成
  font = pygame.font.Font(None, 30)

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

    # 戦闘画面を描画
    draw_battle(screen, font)
    # tmrを１増やす
    tmr = tmr + 1
    # リストkeyに全てのキーの状態を代入
    key = pygame.key.get_pressed()

    # 戦闘開始
    if idx == 10:
      if tmr == 1: set_message("Encounter!")
      if tmr == 6:
        idx = 11
        tmr = 0
    # プレイヤー入力待ち
    elif idx == 11:
      if tmr == 1: set_message("Your turn.")
      # 戦闘コマンドの表示
      battle_command(screen, font)
      # Aキーかスペースキーが押されたら
      if key[K_a] == 1 or key[K_SPACE] == 1:
        idx = 12
        tmr = 0
    # プレイヤーの攻撃
    elif idx == 12:
      if tmr == 1: set_message("You attack!")
      # tmrが２か４なら
      if 2 <= tmr and tmr <= 4:
        # 攻撃エフェクトを描画
        screen.blit(imgEffect, [700-tmr*120, -100+tmr*120])
      if tmr == 5:
        # 敵を点滅させる変数に値をセット
        emy_blink = 5
        set_message("***pts of damage!")
      if tmr == 16:
        idx = 13
        tmr = 0
    # 敵のターン、敵の攻撃
    elif idx == 13:
      if tmr == 1: set_message("Enemy turn.")
      if tmr == 5:
        set_message("Enemy attack!")
        emy_Step = 30
      if tmr == 9:
        set_message("***pts of damage!")
        # 画面を揺らす変数に値をセット
        dmg_eff = 5
        emy_Step = 0
      if tmr == 20:
        idx = 11
        tmr = 0

    # 画面を更新
    pygame.display.update()
    # フレームレートを５秒に設定
    clock.tick(5)

if __name__ == '__main__':
  main()