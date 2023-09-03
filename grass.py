#Importing the Pokemon class and the random module

from pokemon import Pokemon
import random


class Grass(Pokemon):
    def __init__(self, name):
        super().__init__(name, 2)
        
    def get_special_menu(self):
        # Returning the special menu of Grass Pokemon
        return "1. Razor Leaf\n2. Solar Beam"
    
    def _special_move(self, opponent, move):
        # Checking which special move was chosen and calling the corresponding method
        if move == 1:
            return self._razor(opponent)
        elif move == 2:
            return self._beam(opponent)
    
    def _razor(self, opponent):
        #Generating random damage value and calculating the effectiveness of the move
        damage = random.randint(1, 5)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        #Making the opponent take the total damage and returning the move result
        opponent._take_damage(total_damage)
        return f"{self._name} used Razor Leaf {opponent._name} took {total_damage} damage ({effectiveness}x effectiveness).",total_damage
    
    def _beam(self, opponent):
        # Generating random damage value and calculating the effectiveness of the move
        damage = random.randint(3, 4)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        #Making the opponent take the total damage and returning the move result
        opponent._take_damage(total_damage)
        return f"{self._name} used Solar Beam! {opponent._name}",total_damage