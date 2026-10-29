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
            self.color=DARKRED
        elif self.turn_order=="second":
            self.color=DARKBLUE
        self.unit_list=[]
        #json関係
        with open(savedatapath,"r",encoding="utf-8")as file:
            self.savedata=json.load(file)
        #初期化時点でセーブデータのユニットリストを使って
        #リストを作る
        #p1=[1,2,2]
        #p2=[2,2,1]
            
    def load_deck(self,sampleunitlist):
        #自分のセーブデータのインデックスを使ってallunitlistヲ参照して
        #インスタンスを実体化する
        # print("デバッグ1")
        #savedata["deck"][index][unit_id]=unitid
        #unitインスタンスを格納したリストを定義
        
        for savedataindex in range(len(self.savedata["deck"])):
            for allunitlistindex in range(len(sampleunitlist)):
                
                sample=sampleunitlist[allunitlistindex]("sample")
                # print("sample"+str(sample.type_id))
                # print("save"+str(self.savedata["deck"][savedataindex]["unit_id"]))
                if self.savedata["deck"][savedataindex]["unit_id"]==sample.type_id:
                    self.unit_list.append(sampleunitlist[allunitlistindex](self.turn_order))
                    # print("デバッグ4")
                    # print(self.unit_list[0].name)
                sample=None
        # print("デバッグ5")
        
            
