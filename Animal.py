#!/usr/bin/env python3

class Animal(object):
    owner = 'jack1'
    #动物的名称
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name = value
    @classmethod
    def get_owner(cls):
        return cls.owner

class Dog(Animal):
    #狗的叫声，继承Animal
    owner = 'jack2'
    def make_sound(self):
        print(self.get_name() + '的叫声是汪汪汪')

class Cat(Animal):
    #猫的叫声，继承Animal
    def make_sound(self):
        print(self.get_name() + '的叫声是喵喵喵')

if __name__ == '__main__':
    #多态
    animals = [Dog('旺财'), Cat('Kitty'), Dog('来福'), Cat('Betty')]
    for animal in animals:
        animal.make_sound()
    print(Dog('旺财').get_owner())
    print(Animal.get_owner())