#This is a Python implementation of a basic Pokemon battle system.

import random


class Pokemon:
    _battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]

    def __init__(self, name, type): #The code defines a Pokemon class and its attributes such as name, type, and hp points.
        self._name = name
        self._type = type
        self._hp = 25

    def hp(self):
        return self._hp

    def get_normal_menu(self):
        return "1. Slam\n2. Tackle"

    def _normal_move(self, opponent, move):
        if move == "slam":
            return self._slam(opponent)
        elif move == "tackle":
            return self._tackle(opponent)
        else:
            return ""

    def _slam(self, opponent):
        dmg = random.randint(1, 8)
        opponent_type = opponent._type
        multiplier = Pokemon._battle_table[self._type][opponent_type]
        total_dmg = int(dmg * multiplier)
        opponent._take_damage(total_dmg)
        return f"{self._name} uses Slam on {opponent._name}. It does {total_dmg} damage. Effective!" if multiplier == 2 else f"{self._name} uses Slam on {opponent._name}. It does {total_dmg} damage. Not effective.",total_dmg

    def _tackle(self, opponent):
        dmg = random.randint(3, 6)
        opponent_type = opponent._type
        multiplier = Pokemon._battle_table[self._type][opponent_type]
        total_dmg = int(dmg * multiplier)
        opponent._take_damage(total_dmg)
        return f"{self._name} uses Tackle on {opponent._name}. It does {total_dmg} damage. Effective!" if multiplier == 2 else f"{self._name} uses Tackle on {opponent._name}. It does {total_dmg} damage. Not effective.",total_dmg

    def get_special_menu(self):         #The code uses a battle table to calculate the effectiveness of a move against a specific type of Pokemon.
        if type == 0:
            return f'Fire.get_special_menu()'
        elif type == 1:
            return f'Water.get_special_menu()'
        elif type == 2:
            return f'Grass.get_special_menu()'
        

    def _special_move(self, opponent, move):
        if type == 0:
            return f'Fire._special_move(self, opponent, move)'
        elif type == 1:
            return f'Water._special_move(self, opponent, move)'
        elif type == 2:
            return f'Grass._special_move(self, opponent, move)'
            

    def attack(self, opponent, move_type, move):   #It also includes methods to attack an opponent using normal or special moves.
        if move_type == "normal":
            return self._normal_move(opponent, move)
        elif move_type == "special":
            return self._special_move(opponent, move)
        else:
            return ""

    def __str__(self):
        return f"{self._name}: {self._hp}/25"

    def _take_damage(self, dmg):   #The damage inflicted on the opponent depends on the type of move and the type of Pokemon being attacked.
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
