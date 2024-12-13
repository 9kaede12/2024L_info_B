# 読み込みモード（r）でフィルを開く
file = open("info_B/L12/file/test.txt", 'r')
# file = open("info_B/L12/test.txt", 'r')
# 変数rlにファイル内の文字列をすべて読み込む
rl = file.readlines()
# ファイルを閉じる
file.close()
# 繰り返しで1行ずつ
for i in rl:
  # 改行コードを削除して出力
  print(i.rstrip("\n"))