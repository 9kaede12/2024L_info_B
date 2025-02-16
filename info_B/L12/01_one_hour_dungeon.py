import pygame
import sys
import random
from pygame.locals import *

# 色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
CYAN  = (  0, 255, 255)
BLINK = [
  (224, 255, 255), (192, 240, 255), (128, 224, 255),
  ( 64, 192, 255), (128, 224, 255), (192, 240, 255)
]

# 画像の読み込み
imgTitle = pygame.image.load("info_B/L12/images/title.png")
imgWall  = pygame.image.load("info_B/L12/images/wall.png")
imgWall2 = pygame.image.load("info_B/L12/images/wall2.png")
imgDark  = pygame.image.load("info_B/L12/images/dark.png")
imgPara  = pygame.image.load("info_B/L12/images/parameter.png")
imgBtlBG = pygame.image.load("info_B/L12/images/btlbg.png")
imgEnemy = pygame.image.load("info_B/L12/images/enemy0.png")
imgItem = [
  pygame.image.load("info_B/L12/images/potion.png"),
  pygame.image.load("info_B/L12/images/blaze_gem.png"),
  pygame.image.load("info_B/L12/images/spoiled.png"),
  pygame.image.load("info_B/L12/images/apple.png"),
  pygame.image.load("info_B/L12/images/meat.png"),
]
imgFloor = [
  pygame.image.load("info_B/L12/images/floor.png"),
  pygame.image.load("info_B/L12/images/tbox.png"),
  pygame.image.load("info_B/L12/images/cocoon.png"),
  pygame.image.load("info_B/L12/images/stairs.png"),
]
imgPlayer = [
  pygame.image.load("info_B/L12/images/mychr0.png"),
  pygame.image.load("info_B/L12/images/mychr1.png"),
  pygame.image.load("info_B/L12/images/mychr2.png"),
  pygame.image.load("info_B/L12/images/mychr3.png"),
  pygame.image.load("info_B/L12/images/mychr4.png"),
  pygame.image.load("info_B/L12/images/mychr5.png"),
  pygame.image.load("info_B/L12/images/mychr6.png"),
  pygame.image.load("info_B/L12/images/mychr7.png"),
  pygame.image.load("info_B/L12/images/mychr8.png"),
]
imgEffect = [
  pygame.image.load("info_B/L12/images/effect_a.png"),
  pygame.image.load("info_B/L12/images/effect_b.png"),
]

# 変数の宣言
# ゲーム全体の速さ（フレームレート）を管理
speed = 1
# ゲームの進行を管理
idx = 0
# ゲームの進行を管理
tmr = 0
# 現在の階層数
floor = 0
# 到達した階層数（最大値）
fl_max = 1
# [welcome to floor*]メッセージを表示する時間
welcome = 0

# 主人公のダンジョン内の位置x座標
pl_x = 0
# 主人公のダンジョン内の位置y座標
pl_y = 0
# 主人公のダンジョン内のむき
pl_d = 0
# 主人公のダンジョン内のアニメパターン
pl_a = 0
# 主人公のライフ最大値
pl_lifemax = 0
# 主人公のライフ
pl_life = 0
# 主人公の攻撃力
pl_str = 0
# 食料
food = 0
# 手に入れたポーション数
potion = 0
# 手にいれた火炎石数
blazegem = 0
# 宝箱を開けたり、繭に乗った時に出てくるもの
treasure = 0

# 敵の名前
emy_name = ""
# 敵のライフ最大値
emy_lifemax = 0
# 敵のライフ
emy_life = 0
# 敵の攻撃力
emy_str = 0
# 敵の画像を戦闘画面に表示するx座標
emy_x = 0
# 敵の画像を戦闘画面に表示するy座標
emy_y = 0
# 敵の表示演出を行うための変数、画像を前後に動かす
emy_step = 0
# 敵の表示演出を行うための変数、点滅
emy_blink = 0

# プレイヤーがダメージを受けた時に画面を揺らす
dmg_eff = 0
# 戦闘コマンドの値を入れる
btl_cmd = 0

# 画像表示用の定数
COMMAND = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]
TRE_NAME = ["Potion", "Blaze gem", "Food spoiled.", "Food +20", "Food +100"]
EMY_NAME = [
  "Green slime", "Red slime", "Axe beast", "Ogre", "Sword man",
  "Death hornet", "Signal slime", "Devil plant", "Twin killer", "Hell"
]

MAZE_W = 11
MAZE_H = 9
# 自動生成する迷路のデータを入れる
maze = []
for y in range(MAZE_H):
  maze.append([0]*MAZE_W)

DUNGEON_W = MAZE_W*3
DUNGEON_H = MAZE_H*3
# 迷路から生成するダンジョンのデータを入れる
dungeon = []
for y in range(DUNGEON_H):
  dungeon.append([0]*DUNGEON_W)

# ダンジョンの自動生成
def make_dungeon():
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
      # 二列目からは左に壁を作らない
      if x > 2:
        d = random.randint(0, 2)
    maze[y+YP[d]][x+XP[d]] = 1

  # 迷路からダンジョンを作る
  # 全体を壁にする
  for y in range(DUNGEON_H):
    for x in range(DUNGEON_W):
      dungeon[y][x] = 9
  # 部屋と通路の配置
  for y in range(1, MAZE_H-1):
    for x in range(1, MAZE_W-1):
      dx = x*3+1
      dy = y*3+1
      if maze[y][x] == 0:
        # 部屋を作る
        if random.randint(0, 99) < 20:
          for ry in range(-1, 2):
            for rx in range(-1, 2):
              dungeon[dy+ry][dx+rx] = 0
        # 通路を作る
        else:
          dungeon[dy][dx] = 0
          if maze[y-1][x] == 0: dungeon[dy-1][dx] = 0
          if maze[y+1][x] == 0: dungeon[dy+1][dx] = 0
          if maze[y][x-1] == 0: dungeon[dy][dx-1] = 0
          if maze[y][x+1] == 0: dungeon[dy][dx+1] = 0

# ダンジョンを描画する
def draw_dungeon(bg, fnt):
  bg.fill(BLACK)
  for y in range(-4, 6):
    for x in range(-5, 6):
      X = (x+5)*80
      Y = (y+4)*80
      dx = pl_x + x
      dy = pl_y + y
      if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H:
        if dungeon[dy][dx] <= 3:
          bg.blit(imgFloor[dungeon[dy][dx]], [X, Y])
        if dungeon[dy][dx] == 9:
          bg.blit(imgWall, [X, Y-40])
          if dy >= 1 and dungeon[dy-1][dx] == 9:
            bg.blit(imgWall2, [X, Y-80])
      # 主人公キャラの表示
      if x == 0 and y == 0:
        bg.blit(imgPlayer[pl_a], [X, Y-40])
  # 四隅が暗闇の画像を重ねる
  bg.blit(imgDark, [0, 0])
  # 主人公の能力を表示
  draw_para(bg, fnt)

# 床にイベントを配置する
def put_event():
  global pl_x, pl_y, pl_d, pl_a
  # 階段の配置
  while True:
    x = random.randint(3, DUNGEON_W-4)
    y = random.randint(3, DUNGEON_H-4)
    if dungeon[y][x] == 0:
      # 階段の周囲を床にする
      for ry in range(-1, 2):
        for rx in range(-1, 2):
          dungeon[y+ry][x+rx] = 0
      dungeon[y][x] = 3
      break
  # 宝箱と繭の配置
  for i in range(60):
    x = random.randint(3, DUNGEON_W-4)
    y = random.randint(3, DUNGEON_H-4)
    if dungeon[y][x] == 0:
      dungeon[y][x] = random.choice([1,2,2,2,2])
  # プレイヤーの初期位置
  while True:
    pl_x = random.randint(3, DUNGEON_W-4)
    pl_y = random.randint(3, DUNGEON_H-4)
    if dungeon[pl_y][pl_x] == 0:
      break
  pl_d = 1
  pl_a = 2

# 主人公の移動
def move_player(key):
  global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life
  global food, potion, blazegem, treasure
  # 宝箱に載った
  if dungeon[pl_y][pl_x] == 1:
    dungeon[pl_y][pl_x] = 0
    treasure = random.choice([0,0,0,1,1,1,1,1,1,2])
    if treasure == 0:
      potion = potion + 1
    if treasure == 1:
      blazegem = blazegem + 1
    if treasure == 2:
      food = int(food/2)
    # アイテム入手もしくはトラップ
    idx = 3
    tmr = 0
    return
  # 繭に載った
  if dungeon[pl_y][pl_x] == 2:
    dungeon[pl_y][pl_x] = 0
    r = random.randint(0, 99)
    # 食料
    if r < 40:
      treasure = random.choice([3,3,3,4])
      if treasure == 3: food = food + 20
      if treasure == 4: food = food + 100
      # アイテム入手もしくはトラップ
      idx = 3
      tmr = 0
    # 敵出現
    else:
      # 戦闘開始
      idx = 10
      tmr = 0
    return
  # 階段に載った
  if dungeon[pl_y][pl_x] == 3:
    # 画面を切り替える
    idx = 2
    tmr = 0
    return

  # 方向キーで上下左右に移動
  x = pl_x
  y = pl_y
  if key[K_UP] == 1:
    pl_d = 0
    if dungeon[pl_y-1][pl_x] != 9:
      pl_y = pl_y - 1
  if key[K_DOWN] == 1:
    pl_d = 1
    if dungeon[pl_y+1][pl_x] != 9:
      pl_y = pl_y + 1
  if key[K_LEFT] == 1:
    pl_d = 2
    if dungeon[pl_y][pl_x-1] != 9:
      pl_x = pl_x - 1
  if key[K_RIGHT] == 1:
    pl_d = 3
    if dungeon[pl_y][pl_x+1] != 9:
      pl_x = pl_x + 1
  pl_a = pl_d*2
  # 移動したら食料の量と体力を計算
  if pl_x != x or pl_y != y:
    # 移動したら足踏みのアニメーション
      pl_a = pl_a + tmr%2
      if food > 0:
        food = food - 1
        if pl_life < pl_lifemax:
          pl_life = pl_life + 1
      else:
        pl_life = pl_life - 5
        if pl_life <= 0:
          pl_life = 0
          pygame.mixer.music.stop()
          # ゲームオーバー
          idx = 9
          tmr = 0

# 影付き文字の表示
def draw_text(bg, txt, x, y, fnt, col):
  sur = fnt.render(txt, True, BLACK)
  bg.blit(sur, [x+1, y+2])
  sur = fnt.render(txt, True, col)
  bg.blit(sur, [x, y])

# 主人公の能力を表示
def draw_para(bg, fnt):
  X = 30
  Y = 600
  bg.blit(imgPara, [X, Y])
  col = WHITE
  if pl_life < 10 and tmr%2 == 0: col = RED
  draw_text(bg, "{}/{}".format(pl_life, pl_lifemax), X+128, Y+6, fnt, col)
  draw_text(bg, str(pl_str), X+128, Y+33, fnt, WHITE)
  col = WHITE
  if food == 0 and tmr%2 == 0: col = RED
  draw_text(bg, str(food), X+128, Y+60, fnt, col)
  draw_text(bg, str(potion), X+266, Y+6, fnt, WHITE)
  draw_text(bg, str(blazegem), X+266, Y+33, fnt, WHITE)

# 戦闘に入る準備をする
def init_battle():
  global imgEnemy, emy_name, emy_lifemax, emy_life, emy_str, emy_x, emy_y
  typ = random.randint(0, floor)
  if floor >= 10:
    type = random.randint(0, 9)
  lev = random.randint(1, floor)
  imgEnemy = pygame.image.load("info_B/L12/images/enemy"+str(typ)+".png")
  emy_name = EMY_NAME[typ] + " LV" + str(lev)
  emy_lifemax = 60*(typ+1) + (lev-1)*10
  emy_life = emy_lifemax
  emy_str = int(emy_lifemax/8)
  emy_x = 440-imgEnemy.get_width()/2
  emy_y = 560-imgEnemy.get_height()

# 敵の体力を表示するバー
def draw_bar(bg, x, y, w, h, val, max):
  pygame.draw.rect(bg, WHITE, [x-2, y-2, w+4, h+4])
  pygame.draw.rect(bg, BLACK, [  x,   y,    w,  h])
  if val > 0:
    pygame.draw.rect(bg, (0,128,255), [x, y, w*val/max, h])

# 戦闘画面の描画
def draw_battle(bg, fnt):
  global emy_blink, dmg_eff
  bx = 0
  by = 0
  if dmg_eff > 0:
    dmg_eff = dmg_eff - 1
    bx = random.randint(-20, 20)
    by = random.randint(-10, 10)
  bg.blit(imgBtlBG, [bx, by])
  if emy_life > 0 and emy_blink%2 == 0:
    bg.blit(imgEnemy, [emy_x, emy_y+emy_step])
  draw_bar(bg, 340, 580, 200, 10, emy_life, emy_lifemax)
  if emy_blink > 0:
    emy_blink = emy_blink - 1
    # 戦闘メッセージの表示
    for i in range(10):
      draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)
    # 主人公の能力を表示
    draw_para(bg, fnt)

# コマンドの入力と表示
def battle_command(bg, fnt, key):
  global btl_cmd
  ent = False
  # Aキー
  if key[K_a]:
    btl_cmd = 0
    ent = True
  # Pキー
  if key[K_p]:
    btl_cmd = 1
    ent = True
  # Bキー
  if key[K_b]:
    btl_cmd = 2
    ent = True
  # Rキー
  if key[K_r]:
    btl_cmd = 3
    ent = True
  # 矢印上キー
  if key[K_UP] and btl_cmd > 0:
    btl_cmd -= 1
  # 矢印下キー
  if key[K_DOWN] and btl_cmd < 3:
    btl_cmd += 1
  if key[K_SPACE] and key[K_RETURN]:
    ent = True
  for i in range(4):
    c = WHITE
    if btl_cmd == i: c = BLINK[tmr%6]
    draw_text(bg, COMMAND[i], 20, 360+i*60, fnt, c)
  return ent

# 戦闘メッセージの表示処理
# 戦闘中のメッセージを入れる
message = [""]*10
def init_message():
  for i in range(10):
    message[i] = ""

def set_message(msg):
  for i in range(10):
    if message[i] == "":
      message[i] = msg
      return
  for i in range(9):
    message[i] = message[i+1]
  message[9] = msg

# メイン処理
def main():
  global speed, idx, tmr, floor, fl_max, welcome, pl_a, pl_lifemax, pl_life
  global pl_str, food, potion, blazegem, emy_life, emy_step, emy_blink, dmg_eff
  dmg = 0
  lif_p = 0
  str_p = 0

  # モジュールの初期化
  pygame.init()
  # ウィンドウに表示されるタイトル指定
  pygame.display.set_caption("One hour Dungeon")
  # 描画画面スクリーンを初期化する
  screen = pygame.display.set_mode((880, 720))
  # clockオブジェクトを作成
  clock = pygame.time.Clock()
  # フォントオブジェクトを作成
  font = pygame.font.Font(None, 40)
  fonts = pygame.font.Font(None, 30)

  # 効果音とジングル
  se = [
    pygame.mixer.Sound("info_B/L12/sound/ohd_se_attack.ogg"),
    pygame.mixer.Sound("info_B/L12/sound/ohd_se_blaze.ogg"),
    pygame.mixer.Sound("info_B/L12/sound/ohd_se_potion.ogg"),
    pygame.mixer.Sound("info_B/L12/sound/ohd_jin_gameover.ogg"),
    pygame.mixer.Sound("info_B/L12/sound/ohd_jin_levup.ogg"),
    pygame.mixer.Sound("info_B/L12/sound/ohd_jin_win.ogg"),
  ]
  # 無限ループ
  while True:
    # pygameのイベントを繰り返しで処理
    for event in pygame.event.get():
      # ウィンドウの閉じるボタンが押された時
      if event.type == pygame.QUIT:
        # pygameの初期化を解除
        pygame.quit()
        # プログラムを終了する
        sys.exit()
      # キーを押すエベントが発生した時
      if event.type == KEYDOWN:
        # Sキーが押された時
        if event.key == K_s:
          # speedを１増やす
          speed = speed + 1
          # ゲーム全体の速さ最大値の場合は
          if speed == 4:
            # １に戻す
            speed = 1

    # tmrを１増やす
    tmr = tmr + 1
    # リストkeyに全てのキーの状態を代入
    key = pygame.key.get_pressed()

    # タイトル画面
    if idx == 0:
      if tmr == 1:
        pygame.mixer.music.load("info_B/L12/sound/ohd_bgm_title.ogg")
        pygame.mixer.music.play(-1)
      screen.fill(BLACK)
      screen.blit(imgTitle, [40, 60])
      if fl_max >= 2:
        draw_text(screen, "You reached floor {}.".format(fl_max), 300, 460, font, CYAN)
      draw_text(screen, "Press space key", 320, 560, font, BLINK[tmr%6])
      if key[K_SPACE] == 1:
        make_dungeon()
        put_event()
        floor = 1
        welcome = 15
        pl_lifemax = 300
        pl_life = pl_lifemax
        pl_str = 100
        food = 300
        potion = 0
        blazegem = 0
        # 「プレイヤーの移動」を代入
        idx = 1
        pygame.mixer.music.load("info_B/L12/sound/ohd_bgm_title.ogg")
        pygame.mixer.music.play(-1)
    # プレイヤーの移動
    elif idx == 1:
      move_player(key)
      draw_dungeon(screen, fonts)
      draw_text(screen, "floor {} ({},{})".format(floor, pl_x, pl_y), 60, 40, fonts, WHITE)
      if welcome > 0:
        draw_text(screen, "Welcome to floor {}.".format(floor), 300, 180, font, CYAN)
    # 画面の切り替え
    elif idx == 2:
      draw_dungeon(screen, fonts)
      if 1 <= tmr and tmr <= 5:
        h = 80*tmr
        pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
        pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
      if tmr == 5:
        floor = floor + 1
        if floor > fl_max:
          fl_max = floor
        welcome = 15
        make_dungeon()
        put_event()
      if 6 <= tmr and tmr <= 9:
        h = 80*(10-tmr)
        pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
        pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
      if tmr == 10:
        # 「プレイヤーの移動」を代入
        idx = 1

    # アイテム入手もしくはトラップ
    elif idx == 3:
      draw_dungeon(screen, fonts)
      screen.blit(imgItem[treasure], [320, 220])
      draw_text(screen, TRE_NAME[treasure], 380, 240, font, WHITE)
      if tmr == 10:
        # 「プレイヤーの移動」を代入
        idx = 1

    # ゲームオーバー
    elif idx == 9:
      if tmr <= 30:
        PL_TURN = [2, 4, 0, 6]
        pl_a = PL_TURN[tmr%4]
        # 倒れた絵
        if tmr == 30: pl_a = 8
        draw_dungeon(screen, fonts)
      elif tmr == 31:
        se[3].play()
        draw_text(screen, "You died.", 360, 240, font, RED)
        draw_text(screen, "Game over.", 360, 380, font, RED)
      elif tmr == 100:
        # 「タイトル画面」を代入
        idx = 0
        tmr = 0

    # 戦闘開始
    elif idx == 10:
      if tmr == 1:
        pygame.mixer.music.load("info_B/L12/sound/ohd_bgm_battle.ogg")
        pygame.mixer.music.play(-1)
        init_battle()
        init_message()
      elif tmr <= 4:
        bx = (4-tmr)*220
        by = 0
        screen.blit(imgBtlBG, [bx, by])
        draw_text(screen, "Encounter!", 350, 200, font, WHITE)
      elif tmr <= 16:
        draw_battle(screen, fonts)
        draw_text(screen, emy_name+" appear!", 300, 200, font, WHITE)
      else:
        # 「プレイヤーのターン」を代入
        idx = 11
        tmr = 0

    # プレイヤーのターン（入力待ち）
    elif idx == 11:
      draw_battle(screen, fonts)
      if tmr == 1: set_message("Your trun.")
      if battle_command(screen, font, key) == True:
        if btl_cmd == 0:
          # 「プレイヤーの攻撃」を代入
          idx = 12
          tmr = 0
        if btl_cmd == 1 and potion > 0:
          # 「Potionを使う処理」を代入
          idx = 20
          tmr = 0
        if btl_cmd == 2 and blazegem > 0:
          # 「blaze gemを使う処理」を代入
          idx = 21
          tmr = 0
        if btl_cmd == 3:
          # 「逃げられうか？」を代入
          idx = 14
          tmr = 0

    # プレイヤーの攻撃
    elif idx == 12:
      draw_battle(screen, fonts)
      if tmr == 1:
        set_message("You attack!")
        se[0].play()
        dmg = pl_str + random.randint(0, 9)
      if 2 <= tmr and tmr <= 4:
        screen.blit(imgEffect[0], [700-tmr*120, -10+tmr*120])
      if tmr == 5:
        emy_blink = 5
        set_message(str(dmg)+"pts of damage!")
      if tmr == 11:
        emy_life = emy_life - dmg
        if emy_life <= 0:
          emy_life = 0
          # 「戦闘勝利」を代入
          idx = 16
          tmr = 0
      if tmr == 16:
        # 「敵のターン、敵の攻撃」を代入
        idx = 13
        tmr = 0

    # 敵のターン、敵の攻撃
    elif idx == 13:
      draw_battle(screen, fonts)
      if tmr == 1:
        set_message("Enemy turn.")
      if tmr == 5:
        set_message(emy_name + " attack!")
        se[0].play()
        emy_step = 30
      if tmr == 9:
        dmg = emy_str + random.randint(0, 9)
        set_message(str(dmg)+"pts of damage!")
        dmg_eff = 5
        emy_step = 0
      if tmr == 15:
        pl_life = pl_life - dmg
        if pl_life < 0:
          pl_life = 0
          # 「戦闘敗北」を代入
          idx = 15
          tmr = 0
      if tmr == 20:
        # 「プレイヤーのターン」を代入
        idx = 11
        tmr = 0

    # 逃げられる？
    elif idx == 14:
      draw_battle(screen, fonts)
      if tmr == 1: set_message("...")
      if tmr == 2: set_message("......")
      if tmr == 3: set_message(".........")
      if tmr == 4: set_message("............")
      if tmr == 5:
        if random.randint(0, 99) < 60:
          # 「戦闘終了」を代入
          idx = 22
        else:
          set_message("You failed to flee.")
      if tmr == 10:
        # 「敵のターン、敵の攻撃」を代入
        idx = 13
        tmr = 0

    # 敗北
    elif idx == 15:
      draw_battle(screen, fonts)
      if tmr == 1:
        pygame.mixer.music.stop()
        set_message("You  lose.")
      if tmr == 11:
        # 「ゲームオーバー」を代入
        idx = 9
        tmr = 29

    # 勝利
    elif idx == 16:
      draw_battle(screen, fonts)
      if tmr == 1:
        set_message("You win!")
        pygame.mixer.music.stop()
        se[5].play()
      if tmr == 28:
        # 「戦闘終了」を代入
        idx = 22
        if random.randint(0, emy_lifemax) > random.randint(0, pl_lifemax):
          # 「レベルアップ」を代入
          idx = 17
          tmr = 0

    # レベルアップ
    elif idx == 17:
      draw_battle(screen, fonts)
      if tmr == 1:
        set_message("Level up!")
        se[4].play()
        lif_p = random.randint(10, 20)
        str_p = random.randint(5, 10)
      if tmr == 21:
        set_message("Max life + "+str(lif_p))
        pl_lifemax = pl_lifemax + lif_p
      if tmr == 26:
        set_message("Str + "+str(str_p))
        pl_str = pl_str + str_p
      if tmr == 50:
        # 「戦闘終了」を代入
        idx = 22

    # Potionボーション
    elif idx == 20:
      draw_battle(screen, fonts)
      if tmr == 1:
        set_message("Potion!")
        se[2].play()
      if tmr == 6:
        pl_life = pl_lifemax
        potion = potion - 1
      if tmr == 11:
        # 「敵のターン、敵の攻撃」を代入
        idx = 13
        tmr = 0

    # Blaze gem火炎石
    elif idx == 21:
      draw_battle(screen, fonts)
      img_rz = pygame.transform.rotozoom(imgEffect[1], 30*tmr, (12-tmr)/8)
      X = 440-img_rz.get_width()/2
      Y = 360-img_rz.get_height()/2
      screen.blit(img_rz, [X, Y])
      if tmr == 1:
        set_message("Blaze gem!")
        se[1].play()
      if tmr == 6:
        blazegem = blazegem - 1
      if tmr == 11:
        dmg = 1000
        # 「プレイヤーの攻撃」を代入
        idx = 12
        tmr = 4

    # 戦闘終了
    elif idx == 22:
      pygame.mixer.music.load("info_B/L12/sound/ohd_bgm_field.ogg")
      pygame.mixer.music.play(-1)
      # 「プレイヤーの移動」を代入
      idx = 1

    draw_text(screen, "[S]peed "+str(speed), 740, 40, fonts, WHITE)

    # 画面を更新する
    pygame.display.update()
    clock.tick(4+2*speed)

# このプログラムが実行されたときに
if __name__ == '__main__':
  # メイン関数を呼び出す
  main()