import pygame
import sys
import math

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
GOLD    = (255, 216,   0)
SILVER  = (192, 192, 192)
COPPER  = (192, 112,  48)

# メイン関数
def main():
  # pygameモジュールの初期化
  pygame.init()
  # ウィンドウに表示するタイトル
  pygame.display.set_caption("初めてのPygame 図形")
  # 描画画面の初期化
  screen = pygame.display.set_mode((800, 600))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
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

    screen.fill(BLACK)

    # 線ラインの描画
    pygame.draw.line(screen, RED, [0, 0], [100, 200], 10)
    pygame.draw.lines(screen, BLUE, False, [[50, 300], [150, 400], [50, 500]])

    # 矩形レクトの描画
    pygame.draw.rect(screen, RED, [200, 50, 120, 80])
    pygame.draw.rect(screen, GREEN, [200, 200, 60, 180], 5)
    # 多角形ポリゴンの描画
    pygame.draw.polygon(screen, BLUE, [[250, 400], [200, 500], [300, 500]], 10)

    # サークル円の描画
    pygame.draw.circle(screen, GOLD, [400, 100], 60)
    # 楕円エリプスの描画
    pygame.draw.ellipse(screen, SILVER, [400-80, 300-40, 160, 80])
    pygame.draw.ellipse(screen, COPPER, [400-40, 500-80, 80, 160], 20)

    # 円弧アークの角度計算
    ang = math.pi*tmr/36
    # 円弧の描画
    pygame.draw.arc(screen, BLUE, [600-100, 300-200, 200, 400], 0, math.pi*2)
    pygame.draw.arc(screen, WHITE, [600-100, 300-200, 200, 400], ang, ang+math.pi*2, 8)

    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()