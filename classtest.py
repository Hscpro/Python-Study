#!/usr/bin/env python3

class NewUser(object):
    group = 'shiyanlou-louplus'
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def __repr__(self):
        return '{}\'s id is {}'.format(self._name, self._id)
    #property装饰器
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print('ERROR')
    # 静态变量
    @classmethod
    def get_group(cls):
        return cls.group
    #静态类
    @staticmethod
    def format_userdata(id, name):
        print('{0}\'s id is {1}'.format(name, id))

class UserData(object):
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self._id, self._name)

if __name__ == '__main__':
    print(NewUser.get_group())
    NewUser.format_userdata(109, 'Lucy')
