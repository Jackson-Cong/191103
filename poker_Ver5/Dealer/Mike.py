# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 发牌员 Mike, 他可以
#   1) 从某副牌中给某人发指定数量的牌
#   2) 按指定人数平均发牌，多余的牌放在一边
# ------------------------(max to 80 columns)-----------------------------------
import random


def deal_to_a_player(deck, deal_num, player_deck):
    'Desc: Deal some cards to a player from a deck'

    for i in range(deal_num):
        picked_card = random.choice(deck)
        player_deck.append(picked_card)
        deck.remove(picked_card)
    # print('\# NOTE: ==debug1: %s' % (player_deck))
    player_deck.sort()
    #print('==debug2: %s' % (player_deck))
    return


def deal_to_multi_players(deck, *players_decks):
    'Desc: Deal to multiple players, deal remained cards into first player'

    player_num = len(players_decks) # 确定玩家人数
    total_cards = len(deck)         # 获取牌的张数
    deal_num = int(total_cards / player_num)    # 计算发给每个玩家的牌数量
    #print('\n===debug1: %d' % (deal_num))

    for pd in players_decks:
        # 为每个玩家发牌
        deal_to_a_player(deck, deal_num, pd)

    # 如果还有剩余的牌，默认发到第一个玩家
    if len(deck) > 0:
        for card in deck:
            players_decks[0].append(card)
        deck = []
        # 对第一个玩家手中的牌重新进行排序
        players_decks[0].sort()

    return
