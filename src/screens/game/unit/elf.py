import pygame
from src.screens.config.config import *
from src.screens.game.unit.unit import*

# unitに必要な引数


class Elf(Unit):
    def __init__(self,owner):
        super().__init__(self,name="elf",type_id=1,hit_point=2,attack_point=1,owner=owner)
    