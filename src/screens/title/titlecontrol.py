import pygame 
from src.screens.config.config import *
import sys
from pygame.locals import *
from src.screens.title.titleproperties import *
#タイトルControlに専用の描画メソッドが必要タイトルに何を書くか？
#
class TitleControl:
    def __init__(self,):
        print("titlectrl_init")
        self.returnstate="title"
        self.is_ok=True
        
    def run(self,):
        #タイトル画面構成の準備
        pygame.init()
        screen=pygame.display.set_mode(SCREEN_SIZE)#セットモードをscreen変数に格納
        pygame.display.set_caption(TITLE)#タイトルバーの設定
        font =pygame.font.SysFont(None,25)#フォントの用意
        #レクト定義
        startbtn=pygame.Rect(0,0,STARTBTN_WIDTH,STARTBTN_HIGHT)#startボタン
        #座標設定
        startbtn.center=(STARTBTNPOSITION)

        #テキスト定義
        starttxt=font.render(STARTTXT,True,(0,0,0))
        starttxtrect=starttxt.get_rect()
        starttxtrect.center=startbtn.center
        #フラグが立っている間はループを続ける
        while self.is_ok==True:
            #タイトル画面の描画
            pygame.time.wait(1)
            #画面初期化 
            screen.fill(WHITE)#画面を塗りつぶし
            
            #レクト描画
            pygame.draw.rect(screen,RED,startbtn)#startボタン描画
            #レクトテキスト接続
            screen.blit(starttxt,starttxtrect)#テキストの座標を右辺のレクトに張り付けた
            #画面を更新
            pygame.display.update()
            #イベント処理
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                #クリック検出
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if startbtn.collidepoint(event.pos):
                        print("ゲームステートがモードセレクトに更新されます")
                        self.returnstate="modeselect"
                        self.is_ok=False
        return self.returnstate
