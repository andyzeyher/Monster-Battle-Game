# Andy Zeyher
# Section 66

from enemy import *


class bee(Enemy):
    # init method
    def __init__(self, n='Bee'):
        self.__name = n
        self.__health = 25
        self.__defense_mode = False

    # getName method to call name of the bee
    def getName(self):
        return self.__name

    # attack method of the monster
    def basicAttack(self, enemy):
        self.__defense_mode = False
        print('Bee stings you!')
        enemy.doDamage(4)

    # method that defines the damage
    def doDamage(self, damage):
        if self.__defense_mode:
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    # getHealth method to display monster health should I need it
    def getHealth(self):
        return self.__health

    # attack method that is used to make life easier due to the multiple attacks of the pelican monster so that I don't
    # have to call any attack methods by mistake and have unintended affects in the hw3 file
    def attack(self, enemy):
        self.basicAttack(enemy)
