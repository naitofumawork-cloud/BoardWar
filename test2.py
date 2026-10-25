import json
from src.screens.config.config import *

with open(fuma_path,"r",encoding="utf-8")as file:
    fuma=json.load(file)
print(fuma["deck"][0]["unit1_id"])