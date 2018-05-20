# Andy Zeyher
# Section 66

from enemy import *
import sys


class hero(Enemy):

    # init method
    def __init__(self, n):
        self.__name = n
        self.__health = 100
        self.__fb = 10
        self.__pn = 6
        self.__defense_mode = False

    # getName method for the hero
    def getName(self):
        return self.__name

    # basicAttack is the hero sword
    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(5)

    # damage method that defines the damage and cuts it in half should the enemy being attack is in a defense position
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    # getHealth to call the users health in the health bar
    def getHealth(self):
        return self.__health

    # potion method that only allows user to use 6 and does not allow health to go above max health
    def usePotion(self):
        self.__defense_mode = False
        if self.__pn >= 1:
            self.__health += 10
            self.__pn -= 1
            print('You drank a potion.')
            if self.__health > 100:
                self.__health = 100
        else:
            print('No potions left!')

    # fireball method that only allows user to use 10
    def useFireball(self, enemy):
        self.__defense_mode = False
        if self.__fb >= 1:
            enemy.doDamage(10)
            self.__fb -= 1
            print('Fireball Attack Successful!')
        else:
            print('No fireballs left!')

    # shield method that cuts damage in half due to hero being in a defense position
    def useShield(self):
        self.__defense_mode = True

    # Attack method that creates the user interface for the player
    def Attack(self, enemy):
        print(self.getName(), ': ', self.getHealth(), '/100 health')
        print('Remaining: ', self.__fb, 'Fireballs, ', self.__pn, 'Potions')
        choice = input('Enter Command: sword shield fireball potion exit\n')
        if choice.lower() == 'sword':
            print('Sword Slash Attack!')
            self.basicAttack(enemy)
        elif choice.lower() == 'shield':
            print('Hide Behind Shield!')
            self.useShield()
        elif choice.lower() == 'fireball':
            self.useFireball(enemy)
        elif choice.lower() == 'potion':
            self.usePotion()
        elif choice.lower() == 'exit':
            print('Thanks for Playing')
            sys.exit(0)
        else:
            print('Invalid Input')
