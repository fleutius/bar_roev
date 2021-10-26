import sys
import random

class Dice:
    def __init__(self, type):
        self.type = type
        self.locked = False
        self.value = 0
        self.announce = 1


    def toggle(self):
        self.locked = False if self.locked else True

    def is_locked(self):
        return self.locked

    def roll(self):
        if self.locked == False:
            self.value = random.randint(1, self.type)

    def get_value(self):
        return self.value

class Player:
    def __init__(self, name):
        self.name = str(name)
        self.turns = 0
        self.score = 0

    def get_score(self):
        return self.score

    def add_turn(self):
        self.turns = self.turns + 1

    def get_turns(self):
        return self.turns

'''
    def roll(self):
        if self.locked == False:
            self.value = random.randint(1, self.type)
            print(self.value)
            if self.value == 2 or 5:
                self.locked = True
                print(f'{self} has been locked')
                return self.announce
            else:
                return

'''


def retry():
    print()
    tryagain = input("Vil du prøve igen? Y/N: ")
    retry = tryagain.lower()
    if retry == "y":
        main()
    else:
        print()
        print("Tak fordi du spillede Bar Røv. Spillet lukkes")
        sys.exit()
