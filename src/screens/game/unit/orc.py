import pygame
from src.screens.config.config import *
from src.screens.game.unit.unit import*

# unitに必要な引数


class Orc(Unit):
    def __init__(self,owner):
        super().__init__(name="orc",type_id=2,hit_point=3,attack_point=2,owner=owner)
    