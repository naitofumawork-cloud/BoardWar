import pygame
from src.screens.config.config import *
import sys
from pygame.locals import *
from src.screens.game.gameproperties import *
from src.screens.game.board import *
from src.screens.game.bench import *
from src.screens.game.player import *

# unitクラスのインポート
from src.screens.game.unit import *
from src.screens.game.unit.elf import *
from src.screens.game.unit.orc import *


class GameControl:
    def __init__(
        self,
    ):
        print("gamectrl_init")
        self.returnstate = "game"
        self.is_ok = True

    def drawallbtn(self, screen, rectlist, COLLAR):
        for i, rect in enumerate(rectlist):
            pygame.draw.rect(screen, COLLAR, rect)  #

    # 関数説明：ボタンとテキストのレクトの座標を同期してから等間隔に設定する
    def btn_txt_positionequally(self, btnlist, txtrectlist, length):
        for i, rect in enumerate(btnlist):

            rect.center = (WIDTH_HALF, i + 1 * length)
            print("座標を設定>" + str(rect.center))
        for i, rect in enumerate(txtrectlist):
            rect.center = btnlist[i].center

    # レクトテキスト接続
    # 関数説明：すべてのテキストをテキストレクトと合わせて画面に張り付ける
    def allblit(self, screen, txts, txtrects):
        for i, text in enumerate(txts):
            screen.blit(text, txtrects[i])
    def create_allunitlist(self,p1unitlist,p2unitlist):
        allunitlist=[]
        for p1unit in p1unitlist:
            allunitlist.append(p1unit)
        for p2unit in p2unitlist:
            allunitlist.append(p2unit)
        for index in range(len(allunitlist)):
            allunitlist[index].instance_id=int(index+1)
            # allunitlist[index].location="Bench"
            # print("unitname"+str(allunitlist[index].name))
            # print("owner"+str(allunitlist[index].owner))
            # print("id"+str(allunitlist[index].instance_id))
        return allunitlist
    # def draw_unit(self,allunitlist):
    #     for unit in allunitlist:
    #         pygame.draw

    # 関数説明：メインループ
    def run(self,):
        # #json関係
        # with open(fuma_path,"r",encoding="utf-8")as file:
        #     fuma=json.load(file)
        # with open(kimu_path,"r",encoding="utf-8")as file:
        #     kimu=json.load(file)

        # タイトル画面構成の準備
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)  # セットモードをscreen変数に格納
        pygame.display.set_caption(TITLE)  # タイトルバーの設定
        font = pygame.font.SysFont(None, 25)  # フォントの用意

        # ボードの用意

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

        # ボタンとテキストの座標同期＆座標を等間隔に設定
        self.btn_txt_positionequally(btnrects, txtrects, 100)

        #インスタンス化
        #比較用
        #def __init__(self,owner,name,type_id,hit_point,attack_point):
        #def __init__(self,owner):
        #super().__init__(self,name="orc",type_id=2,hit_point=3,attack_point=2,owner=owner)
        
        sampleunitlist = [Elf,Orc]#インスタンス生成クラスのみリスト
        #プレイヤーのユニットデータをインスタンス化する
        #それぞれのユニットにはオーナー情報が保存される
        #その状態のユニットをplayer1~2全てのユニットインスタンスをリストに入れて
        #被らないインスタントIDを振り分ける
        
        # ゲームに使用する全てのユニットのインスタンスをまとめたリスト作りインスタントな番号を割り当てる
        board = Board(5, 5)
        player1 = Player("first", fuma_path)
        player1.load_deck(sampleunitlist)
        player2 = Player("second", kimu_path)
        player2.load_deck(sampleunitlist)
        
        #両プレイヤーの全ユニットを格納
        allunitList=self.create_allunitlist(player1.unit_list,player2.unit_list)
        allaliveunitList=allunitList
        # インスタンス化のロジック

        bench1 = Bench(5, 1, player1)
        bench2 = Bench(5, 1, player2)
        while self.is_ok == True:
            # タイトル画面の描画
            pygame.time.wait(1)
            # 画面初期化
            screen.fill(WHITE)  # 画面を塗りつぶし
            #!!!!!!!描画処理はこれ以降に書く必要あり!!!!!!!
            #ボードの描画処理
            board.drawboard(screen)
            # ベンチインスタンスの生成
            bench1.drawbench(screen, -50, 95)
            bench2.drawbench(screen, 1000, -90)
            #ユニットの描画処理
            # 全ユニットのリストを使って生きてるものだけ各自の場所に描画するallunitlistを使って描画する

            # レクト描画
            # まとめてrectdrawする関数
            self.drawallbtn(screen, btnrects, RED)

            # レクトテキスト接続関数
            # screen.blit(battletxt,battletxtrect)
            self.allblit(screen, txts, txtrects)
            #unitが動く処理（テスト）
            

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
                        self.returnstate = "game"
                        self.is_ok = False
                    #unitclick
                    for x in range(len(allaliveunitList)):
                        if allaliveunitList[x].rect.collidepoint(event.pos):
                            print(allaliveunitList[x].name)
                            allaliveunitList[x].is_drag=True
                            allaliveunitList[x].color=allaliveunitList[x].drag_color
                elif event.type==pygame.MOUSEBUTTONUP:
                    if event.button==1:
                        for x in range(len(allaliveunitList)):
                            if allaliveunitList[x].is_drag==True:
                                print("外れた")
                                allaliveunitList[x].color=allaliveunitList[x].default_color
                                allaliveunitList[x].is_drag=False

            
            # for x in range(len(allaliveunitList)):
            #     if allaliveunitList[x].is_drag==True:
            #         print(str(allaliveunitList[x].name)+"はドラッグ中")
                            
        return self.returnstate


# ゲームループポック
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
