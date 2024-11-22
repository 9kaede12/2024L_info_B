import pygame
import sys
import math

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)

# メイン関数
def main():
  # pygameモジュールの初期化
  pygame.init()
  # ウィンドウに表示するタイトル
  pygame.display.set_caption("初めてのPygame キー入力")
  # 描画画面の初期化
  screen = pygame.display.set_mode((800, 600))
  # clockオブジェクトの作成
  clock = pygame.time.Clock()
  # フォントオブジェクトを作成
  font = pygame.font.Font(None, 60)

  # 無限ループ
  while True:
    # pygameのイベントを繰り返す
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # リストkeyに全てのキーの状態を入力
    key = pygame.key.get_pressed()
    # 方向キー上下のリストの値を描いたSurface
    txt1 = font.render("UP"+str(key[pygame.K_UP])+" DOWN"+str(key[pygame.K_DOWN]), True, WHITE, GREEN)
    # 方向キー左右のリストの値を描いたSurface
    txt2 = font.render("LEFT"+str(key[pygame.K_LEFT])+" RIGHT"+str(key[pygame.K_RIGHT]), True, WHITE, BLUE)
    # スペースキーとEnterキーのリストの値を描いたSurface
    txt2 = font.render("SPACE"+str(key[pygame.K_SPACE])+" ENTER"+str(key[pygame.K_RETURN]), True, WHITE, RED)

    screen.fill(BLACK)
    screen.blit(txt1, [100, 100])
    screen.blit(txt2, [100, 200])

    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()