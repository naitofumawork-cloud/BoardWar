import pygame
from src.screens.config.config import *
from src.screens.game.unit import*
from src.screens.game.cell import*

class Bench:
    def __init__(self,x,y,owner,startx,starty):#引数で縦横長を受け取る
        self.x=x#ベンチの広さ
        self.y=y#ベンチの広さ
        self.owner=owner
        self.unit_list=owner.unit_list
        #引数で受け取ったプレイヤーのデッキデータをもとにユニットのインスタンスを生成してリスへの代入を行う
        
        self.grid=[[0 for j in range(self.x)] for i in range(self.y)]#引数で指定された広さの二次元配列
        for row in range(self.y):
            for column in range(self.x):
                self.grid[row][column]=Cell(row+1,column+1,startx,starty)
                self.unit_list[column].rect.center=self.grid[row][column].rect.center
                 
    #プレイヤーデータからユニットインスタンスを生成する手立て
    #データからidを確認する
    #テーブルは無いのでゲーム開始時に配列を初期化時に作っておくべきか？
    
    #ベンチ（持ち駒を置く場所）を描画する処理  
    def drawbench(self,screen):
        #ベンチの枠の描画
        for row in range(self.y):
            for column in range(self.x):                
                # self.grid[row][column]=Cell(row+1,column+1,-50,300)
                pygame.draw.rect(screen,self.owner.color,self.grid[row][column].rect,5)
                # self.unit_list[column].bench_index=column+1
                # print(column)
                # pygame.draw.rect(screen,self.unit_list[column].color,self.unit_list[column].rect)
                #テスト
    
    """
    座標が変わったときは？
    dragドロップで話した時のレクトを取得その座標をユニットの座標に上書きする
    描画は生きてるunitを今の座標にいるレクトとcenter同期して行う
    """
    
