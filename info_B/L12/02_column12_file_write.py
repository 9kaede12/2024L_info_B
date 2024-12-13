# 書き込みモード（w）でファイルを開く
file = open("info_B/L12/file/test.txt", 'w')
# file = open("info_B/L12/test.txt, 'w")
# 繰り返し　iは０から９まで１ずつ増える
for i in range(10):
  # 文字列をファイルに書きこむ
  file.write("line "+str(i)+"\n")
  # file.write("line "+str(i))
# ファイルを閉じる
file.close()