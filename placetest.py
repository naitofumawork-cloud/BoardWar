import sys
import pygame
from pygame.locals import *
from src.screens.config.config import*#設定ファイル
from src.screens.utils import*
from src.screens.controlmanager import*
pygame.init()


# タイトル画面構成の準備
screen = pygame.display.set_mode((1000,800))  # セットモードをscreen変数に格納
pygame.display.set_caption("テスト")  # タイトルバーの設定
font = pygame.font.SysFont(None, 25)  # フォントの用意
#ボードの用意

# レクト定義
battlebtn = pygame.Rect(0, 0, BTNWIDTH, BTNHIGHT)  # キャラクター
testA = pygame.Rect(0, 0, BTNWIDTH, BTNHIGHT)  # キャラクター
# レクトをリストに格納e
btnrects = [battlebtn]

# テキスト定義
battletxt = font.render(BATTLE, True, (0, 0, 0))
battletxtrect = battletxt.get_rect()
battletxtrect.center = battlebtn.center
# テキストをリストに格納
txts = [battletxt]
# テキストレクトをリストに格納
txtrects = [battletxtrect]


while True:
    
    
        # タイトル画面の描画
    pygame.time.wait(1)
    # 画面初期化
    screen.fill((255,255,255))    

    # 画面を更新
    pygame.display.update()
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # クリック検出
        if event.type == pygame.MOUSEBUTTONDOWN:
            if battlebtn.collidepoint(event.pos):
                print("ゲームステートがバトルに更新されます")

            #unitclick

        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                pass
                # for x in range(len(allaliveunitList)):
                #     if allaliveunitList[x].is_drag==True:
                #         print("外れた")
                #         allaliveunitList[x].color=allaliveunitList[x].default_color
                #         allaliveunitList[x].is_drag=False
                #         print(len(bench1.unit_list))
                #         bench1.unit_list.pop(0)
                #         print(len(bench1.unit_list))
            