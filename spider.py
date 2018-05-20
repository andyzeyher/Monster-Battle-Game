# Andy Zeyher
# Section 66

from enemy import *


class spider(Enemy):

    # init method
    def __init__(self, n='Spider'):
        self.__name = n
        self.__health = 30
        self.__defense_mode = False

    #getName method
    def getName(self):
        return self.__name

    # basic attack method
    def basicAttack(self, enemy):
        self.__defense_mode = False
        print('Spider bites you!')
        enemy.doDamage(5)

    # damage method that defines the damage
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    # getHealth method
    def getHealth(self):
        return self.__health

    # attack method that makes life easier due to the multiple attacks of the pelican
    def attack(self, enemy):
        self.basicAttack(enemy)
