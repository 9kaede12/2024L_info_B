import pygame
import sys

WHITE = (255, 255, 255)
NAVY  = (  0,   0, 128)

# メイン関数
def main():
  # pygameモジュールの初期化
  pygame.init()
  # ウィンドウに表示するタイトル
  pygame.display.set_caption("初めてのPygame 画像の回転、拡縮")
  # 描画画面の初期化
  screen = pygame.display.set_mode((600, 400))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  font = pygame.font.Font(None, 40)
  # キャラクター画像の読み込み
  img = pygame.image.load("info_B/L10/images/pg_slime.png")
  # 時間を管理する変数
  tmr = 0

  # 無限ループ
  while True:
    # １ずつ加算する
    tmr = tmr + 1
    # pygameのイベントを繰り返す
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    ang = (tmr%36)*10
    per = (tmr%100)/20
    # 拡大縮小 [幅、高さ]
    img_s = pygame.transform.scale(img, [70, 92])
    # 回転 回転角
    img_r = pygame.transform.rotate(img, ang)
    # 回転＋拡大縮小 回転角、大きさの比率
    img_rz = pygame.transform.rotozoom(img, ang, per)

    screen.fill(NAVY)
    screen.blit(img   , [100, 100])
    screen.blit(img_s , [200, 100])
    screen.blit(img_r , [300, 100])
    screen.blit(img_rz, [400, 100])

    txt = font.render(str(tmr), True, WHITE)
    # 画像を描画
    screen.blit(txt, [50, 50])

    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()