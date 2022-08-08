from character import Player


class Battle:
    def __init__(self, allies: Player, opponent: list):
        self.allies = allies
        self.opponent = opponent

    def start(self):
        while self.allies.health > 0 and len(self.opponent) > 0:
            self.player.attack(self.opponent)
            if self.opponent.health > 0:
                self.opponent.attack(self.player)
        if self.player.health > 0:
            print('You win')
        else:
            print('You lose')
