import sys
import pygame
from pygame.locals import *
from src.config import*#設定ファイル
from src.utils import*
from src.enemy import*
pygame.init()
def main():
    #準備
    screen=pygame.display.set_mode(SCREEN_SIZE)#セットモードをscreen変数に格納
    pygame.display.set_caption(TITLE)#タイトルバーの設定
    font =pygame.font.SysFont(None,25)#フォントの用意
    #レクト定義
    player=pygame.Rect(0,0,50,50)#キャラクター
    reset=pygame.Rect(WIDTH_8_10,HIGHT_1_10,50,50)
    enemy=Enemy((500,600,))
    #ベルトの状態
    app_state="title"
    ##状態一覧"title","prepare","game"
    
    ##変数定義
    hp=HP#初期HPで初期化
    Timeremaining=TIMEREMAINING
    is_draw=True
    playerposition=PLAYERPOSITION#初期座標
    clampedposition=CLAMPEDPOSITION#初期移動制限座標
    
    #テキストの設定
    text1=font.render(app_state,True,(0,0,0))
    text_hp=font.render("HP"+str(hp),True,GREEN)#テキスト定義
    text_hp_rect=text_hp.get_rect()#レクトを取得してレクトインスタンスとして代入
    text_hp_rect.center=(100,100)#レクトの座標を設定

    fade_count=0  
    #レクトの座標初期化
    player.center=playerposition
    #プレイヤーの座標
    list_s=[]
    list_s.append(reset)
    while True:
        pygame.time.wait(1) 
        screen.fill(WHITE)#画面を塗りつぶし
        #座標更新
        player.center=playerposition
        #レクト描画
        pygame.draw.rect(screen,RED,player)#プレイヤーの描画
        ##試験
        enemy.draw(screen)
        reset.center=(WIDTH_8_10,HIGHT_1_10)
        screen.blit(text1,(40,45))
        screen.blit(text_hp,text_hp_rect)
        
        ##この辺にプレイヤーの座標を引数にして描画しなおす処理を入れたい
        pygame.display.update()#画面を更新
        #イベント処理
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #クリック検出
            if event.type==pygame.MOUSEBUTTONDOWN:
                if reset.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    print("リセットが押された")
                    

if __name__=="__main__":
    main()
