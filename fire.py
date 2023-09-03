#Define the Fire class that inherits from the Pokemon class

from pokemon import Pokemon
import random

class Fire(Pokemon):
    #The Fire class has a type of 0 (Fire) and implements two special moves: Ember and Fire Blast

    def __init__(self, name):
        super().__init__(name, 0)
        
    def get_special_menu(self):
        return "1. Ember\n2. Fire Blast"
    
    def _special_move(self, opponent, move):    #The special moves return a tuple with a string message and the amount of damage dealt to the opponent.
        if move == 1:
            return self._ember(opponent)
        elif move == 2:
            return self._fire_blast(opponent)
    
    def _ember(self, opponent):
        damage = random.randint(1, 5)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]   #The effectiveness is determined using a battle table defined in the Pokemon class and accessed through the _battle_table class variable
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Flamethrower! {opponent._name} took {total_damage} damage ({effectiveness}x effectiveness).",total_damage
    
    def _fire_blast(self, opponent):
        damage = random.randint(3, 4)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]   #The effectiveness is determined using a battle table defined in the Pokemon class and accessed through the _battle_table class variable
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Fire Punch! {opponent._name}",total_damage





