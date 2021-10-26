'''
Projekt 2 - Uge 43
Bar Røv Python program
Flemming, Elisabeth, Anders, Daniel Egelund
'''

# IMPORTS
from bar_resources import Dice
from bar_resources import retry
from bar_resources import Player
import sys
import random

# Spilles med 5 terninger(6 sider) og mindst 2 spillere
# REGLER:
# Så mange point som muligt og først komme op på fas
#
#
# 5 alm terninger



def dice_roll():
    dice_list = [d1, d2, d3, d4, d5]
    avail_dice = 0
    player_score = 0
    times_rolled = 0
    for d in dice_list:
        if d.locked is False:
            avail_dice += 1
    print(f'{avail_dice} avail_dice')
    while avail_dice >= 1:
        for i in range(avail_dice):
            d.roll()
            this_roll = []
            if d.get_value() == 2:
                avail_dice -= 1
                times_rolled += 1
                print(f'der blev rullet {d.get_value()}')
                print("Terningen ramte 2, og gemmes")
                print()
            elif d.get_value() == 5:
                avail_dice -= 1
                times_rolled += 1
                print(f'der blev rullet {d.get_value()}')
                print("Terningen ramte 5, og gemmes")
                print()
            else:
                player_score += d.value
                times_rolled += 1
                print(f'der blev rullet {d.get_value()} din score er nu {player_score}')
                print()

            print(f'der er {avail_dice} terninger tilbage')

    print(f'Der blev rullet i alt {times_rolled} gange, og spiller ')

def player_turn():
    player_count = int(input("Hvor mange spillere er i: "))
    player_list = []
    active_player = []
    for x in range(player_count):
        player_name = f'player{x+1}'
        player = Player(player_name)
        player_list.append((f'player{x+1}'))
    print(str(player_list))

def main_test():
    points_needed = int(input("Hvor mange point skal spillet gå til (50, 100, eller vælg selv): "))
    player_count = int(input("Hvor mange spillere er i: "))
    player_list = []
    d1 = Dice(6)
    d2 = Dice(6)
    d3 = Dice(6)
    d4 = Dice(6)
    d5 = Dice(6)
    for i in range(player_count):
        player_list.append("player {}".format(i + 1))

    dice_roll()








player_turn()

# Point fastsættelse (50, 100, ...)
# Fastsætter antal spillere
# Spiller efter tur, første slag = ALLE terninger

# Slag med  terninger med værdi på enten 2 eller 5, giver IKKE point, og terninger med 2 eller 5 låses
# Der slåes med  de resterende terninger
# Et slag uden 2 eller 5 værdier, giver point, summen af øjnene, er point
# Der slåes indtil alle terninger er væk (låst)
# Når alle terninger har værdi på enten 2 eller 5, er det BAR RØV, og tur går videre
# Sum af point noteres for hver afsluttet runde
# Når der i en runde er mindst 1 spiller som har opnået aftalt point, spilles runden færdig, og point sum afgør spil
