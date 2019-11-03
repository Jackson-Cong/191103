# -*- coding: UTF-8 -*-


import time
import os

# import our modules
from display.menu import *
from display.show import *

from Machine.standard_machine import*

# Phase 1-----------------------------------------------------------------------
# 打印开始界面
dsp_start()
time.sleep(1)  # 延迟3秒

# Phase 2-----------------------------------------------------------------------
# 打印选择游戏玩法界面
game_type = dsp_choice_game()

deck = []
if (game_type == 1 or game_type == 2 or game_type == 3 or game_type == 4):
    make_deck_by_type(game_type, deck)
else:
    dsp_end()
    exit()

# Phase 4-----------------------------------------------------------------------
#预先准备4+1个位置放牌
player_a =[]
player_b =[]
player_c =[]
player_d =[]
player_dumy =[] # 放置预留牌的位置
