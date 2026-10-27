import pygame
from src.screens.config.config import *
from src.screens.game.unit import*
from src.screens.game.cell import*

class Bench:
    def __init__(self,x,y,owner):#引数で縦横長を受け取る
        self.x=x#ベンチの広さ
        self.y=y#ベンチの広さ
        self.owner=owner
        self.unit_list=[]
        #引数で受け取ったプレイヤーのデッキデータをもとにユニットのインスタンスを生成してリスへの代入を行う
        
        self.grid=[[0 for j in range(self.x)] for i in range(self.y)]#引数で指定された広さの二次元配列
    
    #プレイヤーデータからユニットインスタンスを生成する手立て
    #データからidを確認する
    #テーブルは無いのでゲーム開始時に配列を初期化時に作っておくべきか？
    
    #ベンチ（持ち駒を置く場所）を描画する処理  
    def drawbench(self,screen,startx,starty):
        #ベンチの枠の描画
        for row in range(self.y):
            for column in range(self.x):
                #print("デバッグ")
                #print(row)
                #print(column)
                self.grid[row][column]=Cell(row+1,column+1,startx,starty)
                # self.grid[row][column]=Cell(row+1,column+1,-50,300)
                pygame.draw.rect(screen,self.owner.color,self.grid[row][column].rect,5)
                #テスト
                # rect=pygame.Rect(,,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
                # pygame.draw.rect(screen,BLUE,rect,)

#ベンチの枠を描画する際に駒も描画したい
#描画関数の引数にベンチの持ち主のユニットリストを渡す
# ロケーションがベンチのものだけを描画する

    # #ベンチ（持ち駒を置く場所）を描画する処理  
    # def drawbench(self,screen,startx,starty):
    #     #ベンチの枠の描画
    #     for row in range(self.y):
    #         for column in range(self.x):
    #             #print("デバッグ")
    #             #print(row)
    #             #print(column)
    #             self.grid[row][column]=Cell(row+1,column+1,startx,starty)
    #             # self.grid[row][column]=Cell(row+1,column+1,-50,300)
    #             pygame.draw.rect(screen,self.owner.color,self.grid[row][column].rect,5)
    #             #テスト
    #             # rect=pygame.Rect(,,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
    #             # pygame.draw.rect(screen,BLUE,rect,)


                

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
