# create class for card type that contains arrays of card type it is effective of ineffective against
class CardType:
    def __init__(self, advantage, disadvantage):
        self.advantage = advantage
        self.disadvantage = disadvantage


# create subclass of card type that contains all info of a card and
class Card:
    def __init__(self, name, card_type, atk, hp, skill):
        self.name = name
        self.card_type = card_type
        self.atk = atk
        self.hp = hp
        self.skill = skill
        self.blocked = False
        self.wounded = False

    #

    # modify atk by given variable(lowering atk is negative=
    def mod_atk(self, mod):
        self.atk = self.atk + mod

    # modify hp by given variable(dmg is negative)
    def mod_hp(self, mod):
        self.hp = self.hp + mod




