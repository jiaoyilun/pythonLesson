# -*- coding: utf-8 -*-


class Person:
    def __init__(self, _name, _age):
        self._name = _name
        self._age = _age

    def sayhello(self):
        print("Hello,My name is " + self._name + " , I'm " + self._age)

    def saygoodbye(self):
        print("See you again ," + self._name)


john = Person("John", "18")
john.sayhello()
john.saygoodbye()

tom = Person("Tom", "20")
tom.sayhello()
tom.saygoodbye()
