# クラスの宣言
class GameCharacter:
  # コンストラクタ
  def __init__(self, job, life):
    # jobという属性に引数の値を代入
    self.job = job
    # lifeという属性に引数の値を代入
    self.life = life

# warriorというオブジェクトを作る
warrior = GameCharacter("戦士", 100)
# warriorのjob属性の出力
print(warrior.job)
# warriorのlife属性の出力
print(warrior.life)