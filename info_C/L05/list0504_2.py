import random

# リストでアルファベットを定義
ALP = ["A", "B", "C", "D", "E", "F", "G"]
# 抜けている文字をランダムで決める
r = random.choice(ALP)
# 変数を宣言
alp = ""
# リストの中身を１つずつiの中に入れる
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
