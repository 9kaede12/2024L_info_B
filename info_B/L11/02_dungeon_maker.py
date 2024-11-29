import pygame
import sys
import random

BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)
GRAY  = ( 96,  96,  96)

# 迷路の横方向の長さ
MAZE_W = 11
# 迷路の縦方以降の長さ
MAZE_H = 9
# 迷路のデータを入れるリスト
maze = []
# リストの初期化
for y in range(MAZE_H):
  maze.append([0]*MAZE_W)

# ダンジョンの横方向の長さ
DUNGEON_W = MAZE_W*3
# ダンジョンの縦方向の長さ
DUNGEON_H = MAZE_H*3
# ダンジョンのデータを入れるリスト
dungeon = []
# リストの初期化
for y in range(DUNGEON_H):
  dungeon.append([0]*DUNGEON_W)

# ダンジョンの壁の画像
imgWall = pygame.image.load("info_B/L11/images/wall.png")
# ダンジョンの床の画像
imgFloor = pygame.image.load("info_B/L11/images/floor.png")

# ダンジョンの自動生成 ダンジョンを作る関数
def make_dungeon():
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

  # 迷路からダンジョンを作る55~77行目が迷路をダンジョンに変換する処理
  # 全体を壁にする
  for y in range(DUNGEON_H):
    for x in range(DUNGEON_W):
      # dungeonの値を全て９（壁）にする
      dungeon[y][x] = 9
  # 部屋と通路の配置
  for y in range(1, MAZE_H-1):
    for x in range(1, MAZE_W-1):
      dx = x*3+1
      dy = y*3+1
      # 迷路のデータを調べ床のマスなら
      if maze[y][x] == 0:
        # 部屋を作るかランダムに決める
        if random.randint(0, 99) < 20:
          for ry in range(-1, 2):
            for rx in range(-1, 2):
              # ３✖︎３マスを床にする
              dungeon[dy+ry][dx+rx] = 0
        # 部屋をつくらないなら通路を作る
        else:
          # ３✖︎３マスを床にする
          dungeon[dy][dx] = 0
          # 迷路の上のマスが床なら
          if maze[y-1][x] == 0:
            # 上に通路を延ばす
            dungeon[dy-1][dx] = 0
          # 迷路の下のマスが床なら
          if maze[y+1][x] == 0:
            # 下に通路を延ばす
            dungeon[dy+1][dx] == 0
          # 迷路の左のマスが床なら
          if maze[y][x-1] == 0:
            # 左に通路を延ばす
            dungeon[dy][dx-1] = 0
          # 迷路の右のマスが床なら
          if maze[y][x+1] == 0:
            # 右に通路を延ばす
            dungeon[dy][dx+1] = 0

# メインんお処理を行う関数
def main():
  # モジュールの初期化
  pygame.init()
  # ウィンドウに表示されるタイトル
  pygame.display.set_caption("ダンジョンを作る")
  # 描画面スクリーンを初期化する
  screen = pygame.display.set_mode((528, 432))
  # clockオブジェクトを作成
  clock = pygame.time.Clock()

  # ダンジョンを作る関数を呼び出す
  make_dungeon()

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
          make_dungeon()

    # 確認用の迷路を表示 二重ループ
    for y in range(MAZE_H):
      # 繰り返しで迷路を描画する
      for x in range(MAZE_W):
        # 描画用のx座標を計算
        X = x*48
        # 描画用のy座標を計算
        Y = y*48
        # 通路であれば
        if maze[y][x] == 0:
          # 水色の視覚で塗る
          pygame.draw.rect(screen, CYAN, [X, Y, 48, 48])
          # 壁であれば
        if maze[y][x] == 1:
          # 灰色の四角で塗る
          pygame.draw.rect(screen, GRAY, [X, Y, 48, 48])

    # ダンジョンを描画する 二重ループ
    for y in range(MAZE_H):
      # 繰り返しで迷路を描画する
      for x in range(MAZE_W):
        # 描画用のx座標を計算
        X = x*16+528
        # 描画用のy座標を計算
        Y = y*16
        # 通路であれば
        if maze[y][x] == 0:
          # 水色の視覚で塗る
          screen.blit(imgFloor, [X, Y])
          # 壁であれば
        if maze[y][x] == 1:
          # 灰色の四角で塗る
          screen.blit(imgWall, [X, Y])

    # 画面を更新
    pygame.display.update()
    # フレームレート１秒間に2回行う
    clock.tick(2)

# このプログラムが直接実行されたとき
if __name__ == '__main__':
  # メイン関数を呼び出す
  main()