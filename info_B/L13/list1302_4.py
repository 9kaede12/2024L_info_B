# クラスの宣言
class GameCharacter:
  # コンストラクタ
  def __init__(self, job, life):
    # jobという属性に引数の値を代入
    self.job = job
    # lifeという属性に引数の値を代入
    self.life = life

  # 属性の値を出力する関数（メソッド）
  def info(self):
    # job属性の値を出力
    print(self.job)
    # life属性の値を出力
    print(self.life)

# human1というオブジェクトを作る
human1 = GameCharacter("戦士", 100)
# human1のinfo()メソッドを実行
human1.info()

# human2というオブジェクトを作る
human2 = GameCharacter("魔法使い", 80)
# human2のinfo()メソッドを実行
human2.info()