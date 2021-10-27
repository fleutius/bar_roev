import random
import sys


class Die:
    dice = []

    def __init__(self, name):
        self.name = name
        self.index = 0
        self.type = 6
        self.locked = False
        self.value = 0
        self.dice.append(self)

    def __repr__(self):
        return f'{self.name}'

    def __iter__(self):
        return self.name

    def __next__(self):
        if self.index < len(self.dice):
            result = (self.name[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

    def toggle(self):
        self.locked = False if self.locked else True

    def roll(self):
        if self.locked is False:
            self.value = random.randint(1, self.type)

    def get_value(self):
        return self.value

    @classmethod
    def add_dice(cls, i):
        for t in range(i):
            die = Die(f'Terning {t + 1}')


class Player:
    players = []

    def __init__(self, name):
        self.name = name
        self.index = len(Player.players)
        self.turns = 0
        self.score = 0
        self.active = False
        self.players.append(self)

    def __repr__(self):
        return f'{self.name}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.players):
            result = (self.name[self.index])
            self.index += 1
            return result
        elif self.index == len(self.players):
            self.index = 0
        else:
            raise StopIteration

    @classmethod
    def add_player(cls, i):
        for t in range(i):
            player = Player(f'Player {t + 1}')

    def get_score(self):
        return self.score

    def add_score(self, scored_points):
        self.score += scored_points

    @classmethod
    def list_players(cls):
        for player in cls.players:
            print(player)


score_limit = 0
score_limit_input = input("Hvad skal der spilles til a/b/c = (Aa-50 point) (b - 100 point) (c - 150 point)")
score_limit_lower = score_limit_input.lower()
try:
    if score_limit_lower == "a":
        score_limit = 50
        print(f'score limit sat til {score_limit}')
    if score_limit_lower == "b":
        score_limit = 100
        print(f'score limit sat til {score_limit}')
    if score_limit_lower == "c":
        score_limit = 150
        print(f'score limit sat til {score_limit}')
except:
    print("Venligst intast enten a, b eller c ")


def throw():
    avail_dice = 0
    times_rolled = 0
    score = 0
    for die in Die.dice:
        if die.locked is False:
            avail_dice += 1
    print(f'Der er {avail_dice} ulåste terninger ')
    while avail_dice >= 1:
        for dice in range(avail_dice):
            die.roll()
            if die.get_value() == 2:
                avail_dice -= 1
                times_rolled += 1
                print(f'der blev rullet {die.get_value()} - Terningen gemmes')
            elif die.get_value() == 5:
                avail_dice -= 1
                times_rolled += 1
                print(f'der blev rullet {die.get_value()} - Terninging gemmes')

            else:
                score += die.get_value()
                times_rolled += 1

                print(f'der blev rullet {die.get_value()} - din score er nu {score}')
    print()
    print(f'Alle terninger er nu låst. Din samlede score i runden var {score} ')
    print(f'Du rullede i alt {times_rolled} gange')
    return score


def play_round():
    for player in Player.players:
        print()
        print(f'Det er spiller {player} tur')
        turn_score = throw()
        player.add_score(turn_score)
        print(player.name, "score -", player.score)
        next(player)

    for player in Player.players:
        if player.score >= score_limit:
            winner = max(Player.players, key=lambda player: player.score)
            print()
            print(f'Spillet er slut!. {winner} har vundet')
            for player in Player.players:
                print(f'{player.name} fik - {player.score} point!')
            #            retry()
            sys.exit()
        else:
            print()
            print("Resultater for runden: ")
            for player in Player.players:
                print(f'{player.name} er på - {player.score} point!')
            print("Ny runde starter: ")
            print()
            play_round()


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


def main():
    Die.add_dice(5)  # Adding dice to game
    p = int(input("Hvor mange spillere er i? "))
    try:
        Player.add_player(p)
    except ValueError:
        print("Fejl i antal spillere, venligst intast et helt tal! ")
    play_round()  # Plays first round with all players


main()
