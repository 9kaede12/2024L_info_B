import random
import time

print("""
石取りゲームのルール：
石の数が乱数で決まります(15~22個)
先攻、後攻もランダムに決まります。
プレイヤーとコンピューターが交互に1〜3個ずつ取ります。
最後の1個を取ることになった方の負けです。
残りが3個以下で全部とってしまうと負けとします。
""")

stone = random.randint(15, 22) # 石の数を決める
turn = random.randint(0, 1) # どちらの番かを乱数で決める
take = 0 # 石を取った数を代入

while stone>0: # 石が０より大きい間繰り返す
    turn = 1 - turn # どちらの番かを変更
    print("-"*40) # 区切り線を出力
    for i in range(stone): # 石の数だけ繰り返す
        print("●", end="") # 改行をなくして1行で出力
    print(" 石の数", stone) # stoneの数を出力

    ### プレイヤー、コンピュータの各ターン処理
    if turn == 0: # プレイヤーの番
        print("あなたの番")
        while True: # 無限ループ
            i = input("いくつ取りますか？")
            """1〜3を入力した時はtakeにその数を入れて無限ループを抜ける
                1〜3以外の時は無限ループを抜けずに再び入力させる"""
            if i == "1" and stone > 0:
                take = 1
                break
            if i == "2" and stone > 1:
                take = 2
                break
            if i == "3" and stone > 2:
                take = 3
                break
        print("あなたは", take, "取りました")
    else: # コンピュータの番
        print("コンピューターの番")
        take = (stone - 1) % 4 # 取る数を勝てる値とする
        if take == 0: # ０になった場合
            take = random.randint(1, 3) # 取る石の数を決める
            if take > stone: take = stone # 残りの数よりも大きくしない
        time.sleep(2)
        print(take, "取りました") # いくつ取ったかを出力

    stone = stone - take # 石の数を減らす
    time.sleep(2)

print("-------------- ゲーム終了 --------------")
if turn==1: # 勝敗を出力
    print("あなたの勝ち！")
else:
    print("コンピューターの勝ち！")