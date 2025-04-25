import random

# プレイヤーの位置を管理
pl_pos = 1
# コンピュータの位置を管理
com_pos = 1
# ぜーたの位置を管理
z_pos = 1

def banmen():
    print("・" * (pl_pos-1) + "P" + "・" * (30-pl_pos) + "Goal")
    print("・" * (com_pos-1) + "C" + "・" * (30-com_pos) + "Goal")
    print("・" * (z_pos-1) + "Z" + "・" * (30-z_pos) + "Goal")

# 盤面表示
banmen()

while True:
    input("Enterを押すとあなたのコマが進みます")
    # プレイヤーのコマを進める
    pl_pos = pl_pos + random.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("あなたの勝ちです！")
        break
    input("Enterを押すとコンピュータのコマが進みます")
    com_pos = com_pos + random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("コンピュータの勝ちです！")
        break
    input("Enterを押すとゼータのコマが進みます")
    z_pos = z_pos + random.randint(1, 6)
    if z_pos > 30:
        z_pos = 30
    banmen()
    if z_pos == 30:
        print("ゼータの勝ちです！")
        break