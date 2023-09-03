#This script defines a Water class that inherits from the Pokemon class.

from pokemon import Pokemon
import random


class Water(Pokemon):
    #This script defines a Water class that inherits from the Pokemon class.
    def __init__(self, name):
        super().__init__(name, 1)
        
    def get_special_menu(self):
        return "1. Water Gun\n2. Bubble Beam"
    
    def _special_move(self, opponent, move):
        if move == 1:
            return self._water_gun(opponent)
        elif move == 2:
            return self._bubble_beam(opponent)
    
    def _water_gun(self, opponent):
        #The _water_gun method calculates the damage of Water Gun move and the effectiveness against the opponent's type.
        damage = random.randint(1, 6)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Water Gunl! {opponent._name} took {total_damage} damage ({effectiveness}x effectiveness).",total_damage
    
    def _bubble_beam(self, opponent):
        #The _bubble_beam method calculates the damage of Bubble Beam move and the effectiveness against the opponent's type.
        damage = random.randint(3, 4)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Bubble Beam! {opponent._name}",total_damage