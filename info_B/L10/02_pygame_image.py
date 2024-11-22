import pygame
import sys

# メイン関数
def main():
  # pygameモジュールの初期化
  pygame.init()
  # ウィンドウに表示するタイトル
  pygame.display.set_caption("初めてのPygame 画像表示")
  # 描画画面の初期化
  screen = pygame.display.set_mode((640, 360))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # 背景画像の読み込み
  img_bg = pygame.image.load("info_B/L10/images/pg_bg.png")
  # キャラクター画像の読み込み
  img_chara = [
    pygame.image.load("info_B/L10/images/pg_chara0.png"),
    pygame.image.load("info_B/L10/images/pg_chara1.png")
  ]
  # 時間を管理する変数
  tmr = 0

  # 無限ループ
  while True:
    # １ずつ加算する
    tmr = tmr + 1
    # pygameのイベントを繰り返す
    for event in pygame.event.get():
      # ウィンドウを閉じる操作がされたとき
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      # キーを押すイベントが発生したとき
      if event.type == pygame.KEYDOWN:
        # F1キーなら
        if event.key == pygame.K_F1:
          # フルスクリーンにする
          screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
        # F2キーかEscキーなら
        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
          # 通常画面に戻す
          screen = pygame.display.set_mode((640, 360))

    # 背景スクロール用の値をtmrから求める
    x = tmr % 160
    # 繰り返しで横に５枚分
    for i in range(5):
      # 背景画像を描画
      screen.blit(img_bg, [i*160-x, 0])
    # キャラクターをアニメーションさせる
    screen.blit(img_chara[tmr%2], [224, 160])
    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()