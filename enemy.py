# Andy Zeyher
# Section 66

import abc

# Abstract Base Class
class Enemy(metaclass=abc.ABCMeta):

    # init method
    def __init__(self, n):
        pass

    # __str__ override
    def __str__(self):
        return "Generic Enemy Class"

    # special attack that is only used by pelican monster
    def specialAttack(self, enemy):
        pass

    # abstact methods that requires all files inheriting from this class to override these
    @abc.abstractmethod
    def getName(self):
        pass

    @abc.abstractmethod
    def basicAttack(self, enemy):
        pass

    @abc.abstractmethod
    def doDamage(self, enemy):
        pass

    @abc.abstractmethod
    def getHealth(self):
        pass

