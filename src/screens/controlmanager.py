import pygame
from src.screens.config.config import*
from src.screens.title.titlecontrol import*
from src.screens.modeselect.modeselectcontrol import*
from src.screens.game.gamecontrol import*
class ControlManager:
    #敵に必要なもの生成される座標
    def __init__(self,app_state):
        self.appstate=app_state
    def call_control(self,):
        print("現在のステートは"+str(self.appstate))
        match self.appstate:
            case "title":
                print("call title")
                titlectrl=TitleControl()
                self.appstate=titlectrl.run()
            case "modeselect":
                modeselectctrl=ModeSelectControl()
                self.appstate=modeselectctrl.run()
                print("modeselect")
            case "game":
                gamectrl=GameControl()
                self.appstate=gamectrl.run()
                print("game")
        return self.appstate
                
    def update(self,is_collide:bool):
        #自分の状態などを更新する
        #当たれば死ぬ
        if not is_collide:#当たってなければ
            self.is_alive=True
        else:
            self.is_alive=False
    def draw(self,screen):
        pygame.draw.rect(screen,(0,255,0),self.rect)
        
    """
    ステータスを引数にしてコントールmanagerを呼ぶ
    ステータスを確認して適切な処理係を呼ぶ
    """
    