import pygame
from src.config import*#設定ファイル

class Enemy:
    #敵に必要なもの生成される座標
    def __init__(self,pop_position:tuple,):
        self.rect=pygame.Rect(0,0,DEFAULTACTORHIGHT,DEFAULTACTORWIDTH)
        self.position=pop_position
        self.rect.center=(self.position)
        self.is_alive=True
        #reset=pygame.Rect(WIDTH_8_10,HIGHT_1_10,50,50)
    def update(self,is_collide:bool):
        #自分の状態などを更新する
        #当たれば死ぬ
        if not is_collide:#当たってなければ
            self.is_alive=True
        else:
            self.is_alive=False
    def draw(self,screen):
        pygame.draw.rect(screen,(0,255,0),self.rect)
        