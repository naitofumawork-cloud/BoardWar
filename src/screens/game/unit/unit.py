import pygame
from src.screens.config.config import *

# unitに必要な引数


class Unit:
    def __init__(self,owner,name,type_id,hit_point,attack_point,color):
        self.rect = pygame.Rect(0, 0, 80, 80)  # unitもレクトを持つべき
        #ユニット種固有値
        self.type_id=type_id
        self.name = name
        self.hit_point = hit_point
        self.attack_point = attack_point
        

        #可変値
        self.owner=owner
        self.current_hit_point=self.hit_point
        self.current_attack_point=self.attack_point
        self.location=""
        #ベンチ、ボード、虚無空間
        self.is_drag=False
        self.xpos = 0
        self.ypos = 0
        self.bench_index=0
        self.isAlive = True
        self.instance_id=0
        self.color=color
        self.default_color=color
        if self.color==RED:
            self.drag_color=RED_DRAG
        elif self.color==GREEN:
            self.drag_color=GREEN_DRAG
        elif self.color==BLUE:
            self.drag_color=BLUE_DRAG
        elif self.color==YELLOW:
            self.drag_color=YELLOW_DRAG
        elif self.color==PURPLE:
            self.drag_color=PURPLE_DRAG
        # RED
        # GREEN
        # BLUE
        # YELLOW
        # PURPLE

    def update(self, is_collide: bool):
        # 自分の状態などを更新する
        # 当たれば死ぬ
        if not is_collide:  # 当たってなければ
            self.is_alive = True
        else:
            self.is_alive = False
    def attack(self,):
        print("")
    def skill(self):
        print("")
    """
    ユニットが動く処理
    毎ループ呼ばれる
    今unitのレクトの上にカーソルがある&クリックされているか？=ドラッグ状態か？
    
    """
    

    def draw(self, screen,allaliveunitList):
        for x in range(len(allaliveunitList)):
            # pygame.draw.rect(screen,self.unit_list[column].color,self.unit_list[column].rect)
            pygame.draw.rect(screen,self.unit_list[x].color,self.unit_list[x].rect)
#メモ
"""

エルフ：Elf

ドワーフの斧兵：Dwarf Axeman（複数形: Dwarf Axemen） / Dwarf Axewielder

オーク：Orc

コボルド：Kobold

リザードマン：Lizardman（複数形: Lizardmen）

セイレーン：Siren

ハーピー：Harpy

アンデッド（Undead）

スケルトン：Skeleton

ゾンビ：Zombie

レイス：Wraith

バンシー：Banshee

デュラハン：Dullahan

リッチ：Lich

ヴァンパイア：Vampire

幻獣・モンスター（Monsters & Mythical Creatures）

フェニックス：Phoenix

ワイバーン：Wyvern

ユニコーン：Unicorn

キメラ：Chimera

グリフォン：Gryphon（Griffin とも表記）

ミノタウロス：Minotaur

ケンタウロス：Centaur

サイクロプス：Cyclops

コカトリス：Cockatrice

ヒュドラ：Hydra

クラーケン：Kraken

スライム：Slime

ミミック：Mimic

マンティコア：Manticore

ガーゴイル：Gargoyle

トレント：Treant（または Treant / Ent）

カーバンクル：Carbuncle

エルフ
ドワーフの斧兵
オーク
コボルド
リザードマン
セイレーン
ハーピー
スケルトン
ゾンビ
レイス
バンシー
デュラハン
リッチ
ヴァンパイア

フェニックス
ワイバーン
ユニコーン
キメラ
グリフォン
ミノタウロス
ケンタウロス
サイクロプス
コカトリス
ヒュドラ
クラーケン
スライム
ミミック
マンティコア
ガーゴイル
トレント
カーバンクル

爆弾魚
エイリアンクイーン
インドラ
インドラダーク
ドラゴンソーサラー
ゾーク
ネクロランナー
スプリンターゴブリン
プリースト
白騎士
森の狩人
見習いユウシャ
青銅の鎧

憑依の魔女
運命の少女
月明かりの戦士
ドラゴン
"""