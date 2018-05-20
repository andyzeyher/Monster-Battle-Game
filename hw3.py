# Andy Zeyher
# Section 66

# imports of all monsters, hero, and abc class
from bee import *
from hero import *
from pelican import *
from snake import *
from spider import *
import sys
import random

random.seed(0)
print('Welcome to Adventure Battle!')
name = input('What is the name of your hero?\n')
print('How many monsters will', name, 'battle?')
monsters_num = int(input())

# shuffles list of all available monsters
available_monsters = [bee(), pelican(), snake(), spider()]
random.shuffle(available_monsters)
battle_monsters = []
player = hero(name)

# depending on amount of monsters being fought, the monsters are picked from the shuffled list and added to another list
# called battle_monsters so I can tell which will be fighting
if monsters_num == 1:
    m1 = available_monsters[0]
    battle_monsters.append(m1)
if monsters_num == 2:
    m1 = available_monsters[0]
    m2 = available_monsters[1]
    battle_monsters.append(m1)
    battle_monsters.append(m2)
if monsters_num == 3:
    m1 = available_monsters[0]
    m2 = available_monsters[1]
    m3 = available_monsters[2]
    battle_monsters.append(m1)
    battle_monsters.append(m2)
    battle_monsters.append(m3)
if monsters_num == 4:
    m1 = available_monsters[0]
    m2 = available_monsters[1]
    m3 = available_monsters[2]
    m4 = available_monsters[3]
    battle_monsters.append(m1)
    battle_monsters.append(m2)
    battle_monsters.append(m3)
    battle_monsters.append(m4)

# for loop that allows the hero to fight all monsters on the battle_monsters list
for monster in battle_monsters:
    print('You have encountered a', monster.getName())
    # while loop that will continue the fight until either the hero or monster dies
    while monster.getHealth() > 0 and hero.getHealth(player) > 0:
        hero.Attack(player, monster)
        monster.attack(player)
        if monster.getHealth() <= 0:
            # message that displays should a monster die
            print('Enemy is defeated!')
        if hero.getHealth(player) <= 0:
            # message that displays should the hero die and the program exits
            print('You are dead.')
            sys.exit(0)

# message that only appears should the hero defeat all enemies
print('You have defeated all enemies and saved the world. Good Job!')
