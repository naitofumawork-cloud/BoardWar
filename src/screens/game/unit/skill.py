from src.screens.game.unit.unit import*
#エルフの遠距離攻撃にも使える関数を作る
"""
引き数を使って
誰に何ダメージを与えるかを決める

"""
def BowShot(target:Unit):#敵ユニットのインスタンスが入る想定
    target.current_hit_point-=1
    