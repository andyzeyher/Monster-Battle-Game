# Andy Zeyher
# Section 66

from enemy import *
import random


class pelican(Enemy):

    # init method
    def __init__(self, n='Pelican'):
        self.__name = n
        self.__health = 35
        self.__defense_mode = False

    # getName method
    def getName(self):
        return self.__name

    # basic attack method
    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(3)
        print('Pelican slaps you!')

    # special attack method
    def specialAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(7)
        print('Pelican throws brick!')

    # damage method that defines the damage
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    # getHealth method for monster
    def getHealth(self):
        return self.__health

    # attack method that randomly chooses between the basic attack (ba) or the special attack (sa)
    def attack(self, enemy):
        moves = ['ba', 'sa']
        x = random.choice(moves)
        if x == moves[0]:
            self.basicAttack(enemy)
        else:
            self.specialAttack(enemy)
