import pygame
import sys
import random

BLACK = (  0,  0,  0)

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
# 主人公の画像
imgPlayer = pygame.image.load("info_B/L11/images/player.png")

# 主人公のx座標ダンジョンのどこの位置にいるか
pl_x = 4
# 主人公のy座標ダンジョンのどこの位置にいるか
pl_y = 4

# ダンジョンの自動生成 ダンジョンを作る関数
def make_dungeon():
  # 柱から壁を伸ばすための値を定義
  XP = [ 0, 1, 0,-1]
  YP = [-1, 0, 1, 0]

  # 周りの壁　
  for x in range(MAZE_W):
    maze[0][x] = 1
    maze[MAZE_H-1][x] = 1
  for y in range(1, MAZE_H-1):
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

# ダンジョンを描画する関数を定義
def draw_dungeon(bg):
  # 指定した色でスクリーン全体をクリアする
  bg.fill(BLACK)
  for y in range(-5, 6):
    for x in range(-5, 6):
      # 描画用のx座標を計算
      X = (x+5)*16
      # 描画用のy座標を計算
      Y = (y+5)*16
      # ダンジョンのマス目のx座標
      dx = pl_x + x
      # ダンジョンのマス目のy座標
      dy = pl_y + y
      # ダンジョンのデータが定義されている範囲で
      if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H:
        # 床であれば
        if dungeon[dy][dx] == 0:
          # 床の画像を描画
          bg.blit(imgFloor, [X, Y])
        # 壁の画像を描画
        if dungeon[dy][dx] == 9:
          # 壁の画像を描画
          bg.blit(imgWall, [X, Y])
      # 主人公の表示　ウィンドウの中央に
      if x == 0 and y == 0:
        # 主人公を描画
        bg.blit(imgPlayer, [X, Y-8])

# 主人公を移動する関数
def move_player():
  # グローバル変数として宣言
  global pl_x, pl_y
  # リストkeyに全てのキーの状態を代入
  key = pygame.key.get_pressed()
  # 方向キー上が押されたなら
  if key[pygame.K_UP] == 1:
    # その方向が壁でなければ
    if dungeon[pl_y-1][pl_x] != 9:
      # y座標を変化させる
      pl_y = pl_y - 1
  # 方向キー下が押されたなら
  if key[pygame.K_DOWN] == 1:
    # その方向が壁でなければ
    if dungeon[pl_y+1][pl_x] != 9:
      # y座標を変化させる
      pl_y = pl_y + 1
  # 方向キー左が押されたなら
  if key[pygame.K_LEFT] == 1:
    # その方向が壁でなければ
    if dungeon[pl_y][pl_x-1] != 9:
      # x座標を変化させる
      pl_x = pl_x - 1
  # 方向キー右が押されたなら
  if key[pygame.K_RIGHT] == 1:
    # その方向が壁でなければ
    if dungeon[pl_y][pl_x+1] != 9:
      # x座標を変化させる
      pl_x = pl_x + 1

# メインの処理を行う関数
def main():
  # モジュールの初期化
  pygame.init()
  # ウィンドウに表示されるタイトル
  pygame.display.set_caption("ダンジョン内を歩く")
  # 描画面スクリーンを初期化する
  screen = pygame.display.set_mode((176, 176))
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

    # 主人公を動かす関数
    move_player()
    # ダンジョンを描画する
    draw_dungeon(screen)
    # 画面を更新する
    pygame.display.update()
    # フレームレート　１秒間に１０回行う
    clock.tick(10)

# このプログラムが直接実行されたとき
if __name__ == '__main__':
  # メイン関数を呼び出す
  main()