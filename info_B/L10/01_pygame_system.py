import pygame
import sys

# 色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# メイン関数
def main():
  # pygameモジュールの初期化
  pygame.init()
  # ウィンドウに表示するタイトル
  pygame.display.set_caption("初めてのPygame")
  # 描画画面の初期化
  screen = pygame.display.set_mode((800, 600))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # フォントオブジェクトの作成
  font = pygame.font.Font(None, 80)
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

    txt = font.render(str(tmr), True, WHITE)
    screen.fill(BLACK)
    screen.blit(txt, [300, 200])
    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()