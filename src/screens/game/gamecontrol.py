import pygame 
from src.screens.config.config import *
import sys
from pygame.locals import *
from src.screens.game.gameproperties import*
from src.screens.game.board import*
from src.screens.game.bench import*
from src.screens.game.player import*
#unitクラスのインポート
from src.screens.game.unit import*
from src.screens.game.unit.elf import*



    

class GameControl:
    def __init__(self,):
        print("gamectrl_init")
        self.returnstate="game"
        self.is_ok=True
    
    
    #[現在は使用していない]関数説明：ボタンの座標を均等に設定する    
    def btnpositionequally(self,btnlist,length):#どのリストをどの高さで分配するか※高さは中央固定
        #説明_引数で受け取ったボタンリストの中央座標を受け取ったもう片方の引数を用いて等間隔で引き離して初期化する
        for i,rect in enumerate(btnlist):
            rect.center(WIDTH_HALF,i*length)
            
    def drawallbtn(self,screen,rectlist,COLLAR):
        for i,rect in enumerate(rectlist):
            pygame.draw.rect(screen,COLLAR,rect)#
            
    #関数説明：ボタンとテキストのレクトの座標を同期してから等間隔に設定する
    def btn_txt_positionequally(self,btnlist,txtrectlist,length):
        for i,rect in enumerate(btnlist):
            
            rect.center=(WIDTH_HALF,i+1*length)
            print("座標を設定>"+str(rect.center))
        for i,rect in enumerate(txtrectlist):
            rect.center=btnlist[i].center
        
    #レクトテキスト接続        
    #関数説明：すべてのテキストをテキストレクトと合わせて画面に張り付ける
    def allblit(self,screen,txts,txtrects):
        for i,text in enumerate(txts):
            screen.blit(text,txtrects[i])
    #関数説明：メインループ
    def run(self,):
        
        
        # #json関係
        # with open(fuma_path,"r",encoding="utf-8")as file:
        #     fuma=json.load(file)
        # with open(kimu_path,"r",encoding="utf-8")as file:
        #     kimu=json.load(file)
        
        
        #タイトル画面構成の準備
        pygame.init()
        screen=pygame.display.set_mode(SCREEN_SIZE)#セットモードをscreen変数に格納
        pygame.display.set_caption(TITLE)#タイトルバーの設定
        font =pygame.font.SysFont(None,25)#フォントの用意
        
        #ボードの用意

        #レクト定義
        battlebtn=pygame.Rect(0,0,BTNWIDTH,BTNHIGHT)#キャラクター
        testA=pygame.Rect(0,0,BTNWIDTH,BTNHIGHT)#キャラクター
        #レクトをリストに格納e
        btnrects=[battlebtn]
        
        #テキスト定義
        battletxt=font.render(BATTLE,True,(0,0,0))
        battletxtrect=battletxt.get_rect()
        battletxtrect.center=battlebtn.center
        #テキストをリストに格納
        txts=[battletxt]
        #テキストレクトをリストに格納
        txtrects=[battletxtrect]
        
        #ボタンとテキストの座標同期＆座標を等間隔に設定
        self.btn_txt_positionequally(btnrects,txtrects,100)
        
        
        #インスタンス化
        allunitlist=
        #ゲームに使用する全てのユニットのインスタンスをまとめたリスト作りインスタントな番号を割り当てる
        #エルフ:1番 ドラゴン:2番　エルフ:3番
        a=Unit()
        f=Elf()
        board=Board(5,5)
        player1=Player("first",fuma_path)
        player1.load_deck()
        player2=Player("second",kimu_path)
        player2.load_deck()
        #インスタンス化のロジック
        
        
        bench1=Bench(5,1,player1)
        bench2=Bench(5,1,player2)
        while self.is_ok==True:
            #タイトル画面の描画
            pygame.time.wait(1)
            #画面初期化 
            screen.fill(WHITE)#画面を塗りつぶし
            #!!!!!!!描画処理はこれ以降に書く必要あり!!!!!!!
            
            board.drawboard(screen)
            #ベンチインスタンスの生成
            bench1.drawbench(screen,-50,95)
            bench2.drawbench(screen,1000,-90)
            #レクト描画
            #まとめてrectdrawする関数
            self.drawallbtn(screen,btnrects,RED)

            #レクトテキスト接続関数
            # screen.blit(battletxt,battletxtrect)
            self.allblit(screen,txts,txtrects)
                    
            #画面を更新
            pygame.display.update()
            #イベント処理
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                #クリック検出
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if battlebtn.collidepoint(event.pos):
                        print("ゲームステートがバトルに更新されます")
                        self.returnstate="game"
                        self.is_ok=False
                ##スイッチが押されたらisOKフラグを下してreturnステートを更新させる
        return self.returnstate
#ゲームループポック
"""
gameに遷移後設定ファイルjsonから現在の敵と自分の持ち駒を読み込んでゲームを開始させる
必要な要素
プレイヤーのインスタンス（自分と相手）
ループ
自分のターン、相手のターンを交互に

ボード
ボードにはコマを動かせる仕組みが必要
コマは
"""


