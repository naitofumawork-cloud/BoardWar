import pygame
from src.screens.config.config import *
import json

# from src.screens.game.unit import*
# from src.screens.game.cell import*
#プレイヤーが持つべき属性
"""
先攻後攻
持ちゴマのリスト
プレイヤーの持ち駒
プレイヤーの

"""

class Player:
    def __init__(self,turn_order,savedatapath):#
        self.turn_order=turn_order#先攻後攻が入る
        
        if self.turn_order=="first":
            self.color=RED
        elif self.turn_order=="second":
            self.color=BLUE
        self.unit_list=[]
        #json関係
        with open(savedatapath,"r",encoding="utf-8")as file:
            self.savedata=json.load(file)
        #初期化時点でセーブデータのユニットリストを使って
        #リストを作る
        #p1=[1,2,2]
        #p2=[2,2,1]
            
    def load_deck(self,allunitlist):
        #自分のセーブデータのインデックスを使ってallunitlistヲ参照して
        #インスタンスを実体化する
        print("デバッグ1")
        #savedata["deck"][index][unit_id]=unitid
        #unitインスタンスを格納したリストを定義
        
        for x in range(len(self.savedata["deck"])):
            for y in range(len(allunitlist)):
                print("デバッグ2"+str(allunitlist[y].name))
        
        
                if x==allunitlist[y].type_id:
                    print("デバッグ3")
                    xx=allunitlist[y]("test")
                    self.unit_list.append(xx)
                    print("デバッグ4")
                    
        print(self.unit_list[0].name)
        print(self.unit_list[1].name)
        print(self.unit_list[2].name)
        print(self.unit_list[2].name)
        print("デバッグ5")
            
        # for unitid in range(len(self.savedata["deck"])):
        #     print("デバッグ開始")
        #     print("インデックスは"+str(unitid))
        #     print(self.savedata["deck"][unitid]["unit_id"])
        #     for index in range(len(allunitlist)):
        #         #self.savedata["deck"][index]["unit_id"]
        #         if self.savedata["deck"][unitid]["unit_id"]==allunitlist[index]:
        #             self.unit_list.append(unit=allunitlist[index]())
        
        # print(self.unit_list)
            

