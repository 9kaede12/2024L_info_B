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

# warriorというオブジェクトを作る
warrior = GameCharacter("戦士", 100)
# warriorのinfo()メソッドを実行
warrior.info()