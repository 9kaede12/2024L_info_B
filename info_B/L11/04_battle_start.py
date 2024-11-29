import pygame
import sys

# 色の定義
WHITE = (255, 255, 255)

# 先頭の背景画像を読み込む
imgBtlBG = pygame.image.load("info_B/L11/images/btlbg.png")
# 敵の画像を読み込むための変数を用意この時点ではなし
imgEnemy = None

# 読み込む画像の番号を管理する変数
emy_num = 0
# 敵キャラクター表示位置のx座標
emy_x = 0
# 敵キャラクター表示位置のy座標
emy_y = 0

# 先頭に入る準備をする関数
def init_battle():
  # グローバル変数の宣言
  global imgEnemy, emy_num, emy_x, emy_y
  # 敵の画像を管理する番号を増やす
  emy_num = emy_num + 1
  # ５になったら
  if emy_num == 5:
    # １に戻す
    emy_num = 1
  # 敵キャラクターの画像を読み込む
  imgEnemy = pygame.image.load("info_B/L11/images/enemy"+str(emy_num)+".png")
  # 表示位置を画像の幅から求める
  emy_x = 440-imgEnemy.get_width()/2
  # 表示位置を画像の高さから求める
  emy_y = 560-imgEnemy.get_height()

# 先頭画面を描画する関数
def draw_battle(bg, fnt):
  # 背景の描画
  bg.blit(imgBtlBG, [0, 0])
  # 敵キャラクターの描画
  bg.blit(imgEnemy, [emy_x, emy_y])
  sur = fnt.render("info_B/L11/images/enemy"+str(emy_num)+".png", True, WHITE)
  # 文字列を書いたSurfaceを画面に表示
  bg.blit(sur, [310, 580])

# メイン関数
def main():
  # モジュールの初期化
  pygame.init()
  # タイトルを設定
  pygame.display.set_caption("戦闘開始の処理")
  # 描画画面の初期化
  screen = pygame.display.set_mode((880, 720))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # フォントオブジェクトの作成
  font = pygame.font.Font(None, 40)

  # 戦闘に入る準備をする関数を呼ぶ
  init_battle()

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
        # スペースボタンが押された時
        if event.key == pygame.K_SPACE:
          # 先頭に入る準備をする関数を実行
          init_battle()

    # 先頭画面を描画
    draw_battle(screen, font)
    # 画面を更新
    pygame.display.update()
    # フレームレートを５秒に設定
    clock.tick(5)

if __name__ == '__main__':
  main()