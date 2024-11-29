import pygame
import sys
import random

CYAN = (  0, 255, 255)
GRAY = ( 96,  96,  96)

# 迷路の横方向の長さ
MAZE_W = 11
# 迷路の縦方以降の長さ
MAZE_H = 9
# 迷路のデータを入れるリスト
maze = []

# リストの初期化
for y in range(MAZE_H):
  maze.append([0]*MAZE_W)

# 迷路を作る関数
def make_maze():
  # 柱から壁を伸ばすための値を定義
  XP = [ 0, 1, 0,-1]
  YP = [-1, 0, 1, 0]

  # 周りの壁　
  for x in range(MAZE_W):
    maze[0][x] = 1
    maze[MAZE_H-1][x] = 1
  for y in range(MAZE_H-1):
    maze[y][0] = 1
    maze[y][MAZE_W-1] = 1

  # 中を何もない状態に
  for y in range(1, MAZE_H-1):
    for x in range(1, MAZE_W-1):
      maze[y][x] = 0

  # 柱
  for y in range(2, MAZE_H-2, 2):
    for x in range(2, MAZE_W-2, 2):
      maze[y][x] = 1

  # 柱から上下左右に壁を作る
  for y in range(2, MAZE_H-2, 2):
    for x in range(2, MAZE_W-2, 2):
      d = random.randint(0, 3)
      if x > 2:
        d = random.randint(0, 2)
      maze[y+YP[d]][x+XP[d]] = 1

# メインんお処理を行う関数
def main():
  # モジュールの初期化
  pygame.init()
  # ウィンドウに表示されるタイトル
  pygame.display.set_caption("迷路を作る")
  # 描画面スクリーンを初期化する
  screen = pygame.display.set_mode((528, 432))
  # clockオブジェクトを作成
  clock = pygame.time.Clock()

  # 迷路を作る関数を呼び出す
  make_maze()

  # 無限ループ
  while True:
    # pygameイベントを繰り返す
    for event in pygame.event.get():
      # ウィンドウを閉じるボタンが押された時
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      # キーを押すイベントが発生した時
      if event.type == pygame.KEYDOWN:
        # スペースがあるならば
        if event.type == pygame.K_SPACE:
          # 迷路を作る関数を実行
          make_maze()

    # 二重ループ
    for y in range(MAZE_H):
      # 繰り返しで迷路を描画する
      for x in range(MAZE_W):
        # １マスの幅
        W = 48
        # １マスの高さ
        H = 48
        # 描画用のx座標を計算
        X = x*W
        # 描画用のy座標を計算
        Y = y*H
        # 通路であれば
        if maze[y][x] == 0:
          # 水色の視覚で塗る
          pygame.draw.rect(screen, CYAN, [X, Y, W, H])
          # 壁であれば
        if maze[y][x] == 1:
          # 灰色の四角で塗る
          pygame.draw.rect(screen, GRAY, [X, Y, W, H])

    # 画面を更新
    pygame.display.update()
    # フレームレート１秒間に2回行う
    clock.tick(2)

# このプログラムが直接実行されたとき
if __name__ == '__main__':
  # メイン関数を呼び出す
  main()