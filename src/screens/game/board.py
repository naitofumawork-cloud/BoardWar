import pygame
from src.screens.config.config import *
from src.screens.game.unit.unit import*
from src.screens.game.cell import*
##ボードに必要な引数
"""
拡張性を持たせるため縦横の升目の長さが必要か？面倒なのでとりあえずは呼ぶときは固定で運用

"""             
class Board:
    def __init__(self,x,y):#引数で縦横長を受け取る
        self.gridwidth=x
        self.gridhight=y
        self.grid=[[0 for j in range(self.gridwidth)] for i in range(self.gridhight)]
        
    def gridinit(self,):
        self.grid=[]

    def showgrid(self,):
        print(self.grid)
        #配列を走査して中にユニットがいればokいないとNoを出すようにする
        for x in range(self.gridwidth):
            for y in range(self.gridhight):
                if type(self.grid[x-1][y-1])==Unit:
                    print(str(x+1)+"行目の"+str(y+1)+"列目はUnit")
                else:
                    print(str(x+1)+"行目の"+str(y+1)+"列目はUnitじゃない")
                    
    def drawboard(self,screen):
        #各レクトに座標を設定する
        testx=100
        standard=testx//2#50
        #50+row*100
        xlength=self.gridwidth*testx
        for row in range(self.gridwidth):
            for column in range(self.gridhight):
                self.grid[row][column]=Cell(row+1,column+1,300,50)
                # self.grid[row][column]=pygame.Rect(350+row*101,100+column*101,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
                pygame.draw.rect(screen,BLACK,self.grid[row][column].rect,5)
                
    #ボードと上に載っているユニットすべてを描画する
    #aliveunitlist=[ユニットのインスタンスたち]
    def draw(self,screen,aliveunitlist):
        for i in range(aliveunitlist):
            #描画座標の決定
            #インスタンスの座標が1,1なら
            aliveunitlist[i].rect.center=()
            pygame.draw.rect(screen,aliveunitlist[i].color,aliveunitlist[i].rect)#
        
        print
    def putunit(self,unit,x,y):
        self.grid[x-1][y-1]=unit
def main():
    board=Board(3,2)
    board.showgrid()
    
    unitA=Unit()
    
    board.putunit(unitA,1,1)
    board.showgrid()
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
