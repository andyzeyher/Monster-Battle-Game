# Andy Zeyher
# Section 66

from enemy import *


class snake(Enemy):

    # init method
    def __init__(self, n='Snake'):
        self.__name = n
        self.__health = 20
        self.__defense_mode = False

    # getName method
    def getName(self):
        return self.__name

    # basic attack method
    def basicAttack(self, enemy):
        self.__defense_mode = False
        print('Snake bites you!')
        enemy.doDamage(5)

    # damage method that defines the damage
    def doDamage(self, damage):
        if self.__defense_mode:
            # Half Damage
            self.__health = self.__health
        else:
            self.__health = self.__health - damage

    # getHealth method
    def getHealth(self):
        return self.__health

    # attack method that makes life easier due to the multiple attacks of the pelican
    def attack(self, enemy):
        self.basicAttack(enemy)
