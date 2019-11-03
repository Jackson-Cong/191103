# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 洗牌机模块之一，可以
#   1) 创建一副标准的 54张牌
#   2) 将这副牌随机洗好
#   3) 可以将一副牌的内容记录到一个指定的文件里
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import copy
import os

# initialize var
cardJokers = ('♞', '♘')
cardMarks = ('♠', '♥', '♣', '♦')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')


def create_deck_54(new_deck):
    'Desc: Make a new standard 54 cards poker, put them in order'
    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    # shuffle_deck(new_deck)
    return

def create_deck_52(new_deck):
    'Desc: Make a new standard 54 cards poker, put them in order'

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    # shuffle_deck(new_deck)
    return


def shuffled_deck(deck):
    'Desc: Shuffle a deck'
    #shuffledDeck = copy.copy(deck)
    random.shuffle(deck)
    return


def record_deck(deck, filename):
    'Desc: Write a deck into a specified file'
    out_path = os.getcwd() + '\\output_decks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck:
        f.write(card)
        f.write('\n')
    f.close()
    return

# ----------------3.0 ----------------------


def make_deck_by_type(play_type, out_deck):
    if play_type == 1:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '争上游-刚洗好的牌.txt')
    if play_type == 2:
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '桥牌-刚洗好的牌.txt')
    if play_type == 3:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '三人斗地主-刚洗好的牌.txt')
    if play_type == 4:
        # first deck
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        # second deck
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        # shuffled & record
        shuffled_deck(out_deck)
        record_deck(out_deck, '四人斗地主-刚洗好的牌.txt')

    return
