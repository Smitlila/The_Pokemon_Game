"""CECS 277

Group 8.5

1) Smit Lila
2) Andrew Molina 

Pokémon Gym Battle 
  
Create a game where the user must defeat three pokémon to win the game.  Use inheritance to 
implement the following class diagram in your program. 


In this project, majority of code has been done by both members,
I (Smit Lila) did pokemon, main, and fire file; and Andrew did others.
"""

import random
from pokemon import Pokemon
from water import Water
from fire import Fire
from grass import Grass
import check_input

def gym_attack(gym_pokemon,gym_pokemon_type,pokemon):       #made an gym_attack function to get random move from a opponent
    gym_attack = random.randint(1,2)
    gym_choice_mov = random.randint(1,2)
    if gym_attack == 1:
        gym_choice_mov = random.randint(1,2)
        if gym_choice_mov == 1:
            mov,dmg = gym_pokemon.attack(pokemon,"normal","slam")   #call attack function from pokemon file 
        elif gym_choice_mov == 2:
            mov,dmg = gym_pokemon.attack(pokemon,"normal","tackle")        
    elif gym_attack == 2:
        if gym_choice_mov == 1:
            mov,dmg = gym_pokemon_type._special_move(pokemon,1)     #call _special_move function from pokemon file
        elif gym_choice_mov == 2:
            mov,dmg = gym_pokemon_type._special_move(pokemon,2)
    return mov,dmg                 #return name of the move and damage of the opponent 

def main():
    print ("PROF OAK:  Hello Trainer!\nToday you're off to fight your first gym battle of 1 vs. 3 GRASS pokemon.\nSelect the pokemon that you will fight with. ")
    print("1. I choose you, Charmander. \n2. Squirtle!  GO! \n3. We can do it, Bulbasaur!")
    
    user_input = check_input.get_int_range("Please choose a pokemon: ",1,3)
    if user_input == '1':
        user_pokemon = Fire("Charmander")   #call fire object if user select charmander
        pokemon = Pokemon("Charmander",0)
    elif user_input == '2':
        user_pokemon = Water("Squirtle")    #call water object if user select squirtle
        pokemon = Pokemon("Squirtle",1)
    else:
        user_pokemon = Grass("Bulbasaur")   #call grass object if user select bulbasaur 
        pokemon = Pokemon("Bulbasaur",2)
    
    
    user_pokemon_hp = int(pokemon._hp)      
    print("  -- GYM BATTLE -- ")
    opponents = ["Oddish","Bellsprout","Chikorita"]
    for i in range(len(opponents)):     #for loop to get each opponent one by one 
        opp = opponents[i] 
        gym_pokemon_type = Grass(opp)          #get opponent type grass using grass object 
        opp_pokemon = Pokemon(opp,2)           #difine opponent as a oposite pokemon 
        gym_pokemon_hp = opp_pokemon._hp
        bool = True
        
        while gym_pokemon_hp > 0 and user_pokemon_hp > 0:       #while loop to run the game till the hp is not 0 
            print()
            print("GYM LEADER: I choose you:")
            print(f"{opp_pokemon._name} HP: {gym_pokemon_hp}/25")
            print()
            print(f'{pokemon._name} HP: {user_pokemon_hp}/25')
            print("Choose an Attack Type: \n1. Normal \n2. Special ")
            user_attack = input("Enter attack type: ")
            if user_attack == '1':
                print("Choose a Move: ")
                print(pokemon.get_normal_menu())        #call get_normal_mennu to get menu from pokemon file
                move = input("Enter move: ")
                if move == '1':
                    mov,dmg = pokemon.attack(opp_pokemon,"normal","slam")   #it will give move  type and damage 
                    print(mov)
                    gym_pokemon_hp -= int(dmg)
                    gym_move,poke_dmg = gym_attack(opp_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
                if move == '2':
                    mov,dmg = pokemon.attack(opp_pokemon,"normal","tackle")
                    print(mov)
                    gym_pokemon_hp -= int(dmg)
                    gym_choice_attack = random.randint(1,2)
                    gym_choice_mov = random.randint(1,2)
                    gym_move,poke_dmg = gym_attack(opp_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
            elif user_attack == '2':
                print("Choose a Move: ")
                print(user_pokemon.get_special_menu())  #Get_special menu to get special menu from pokemon file 
                sp_move = input("Enter move: ")
                if sp_move == '1':
                    sp_mov,sp_dmg = user_pokemon._special_move(opp_pokemon,1)
                    print(sp_mov)
                    gym_pokemon_hp -= int(sp_dmg)
                    gym_move,poke_dmg = gym_attack(opp_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
                elif sp_move == '2':
                    sp_mov,sp_dmg = user_pokemon._special_move(opp_pokemon,2)
                    print(sp_mov)
                    gym_pokemon_hp -= int(sp_dmg)
                    gym_move,poke_dmg = gym_attack(opp_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
            if user_pokemon_hp <= 0:
                print()
                print(f"YOU LOSS! {opp_pokemon._name} defeat {user_pokemon._name} !!!!!!!!!!")
                break
                
            if gym_pokemon_hp <= 0:
                print()
                print(f"YOU WON!  You defeated {opp_pokemon._name} !!!!!!!! ") 
                 
main()