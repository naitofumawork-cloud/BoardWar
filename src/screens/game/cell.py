import pygame
from src.screens.config.config import *
from src.screens.game.unit import*

class Cell:
    def __init__(self,posx,posy,startx,starty):#引数で縦横長を受け取る
        self.posx=posx
        self.posy=posy
        self.rect=pygame.Rect(startx+posx*101,starty+posy*101,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
        # self.rect=pygame.Rect(300+x*101,50+y*101,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
        self.isPlaced=False#unitが置かれたかどうかのフラグ
                    
    def putunit(self,unit,x,y):
        self.grid[x-1][y-1]=unit
# def main():
#     board=Board(3,2)
#     board.showgrid()
    
#     unitA=Unit()
    
#     board.putunit(unitA,1,1)
#     board.showgrid()
"""
ボードに必要な所作ユニットが置けるユニットの手持ちを置く台が必要
処理の実装
ユニットを置く台でユニットのレクトの上にホバー状態のときにクリックを続けるとドラッグ状態として判定する
ドラッグ状態はユニットの描画はマスから消えてマウスに追従する形をとる
ドラッグ中もグリッドのどのマスの上にホバー中か？を判断する
もし空のマスならそこにユニットは移動する
内部的には
台の上にユニットリストからリムーブして
盤所のユニットリストへムーブする
そしてその時にユニットインスタンスの座標プロパティは
ホバーを離したグリッドの座標を代入する
つまりますめもインスタンスである必要がある
升目のプロパティ
XY座標、ユニットが置かれいてるかのフラグ等
が必要
"""
"""
セルがホバー判定されるべき時
ユニットを移動させるとき
ユニットを置くとき
技の座標を決めるとき
マスをホバーさせてそのマスの情報を見たいとき
罠があるとか燃えてるとか
結論はいつでもホバーかどうかは見えるべき
ホバー判定メソッドを作って
毎ループ呼ばせる
"""
