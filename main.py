from events import *
from random import choice


class Character:
    def __init__(self, name, age, strength, dexterity, intellingence):
        self.name = name
        self.age = age
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intellingence


def char():
    name = input("Имя персонажа: ")
    age = int(input("Возраст персонажа: "))
    strength = int(input("Сила персонажа (от 1 до 10): "))
    if strength > 10 or strength < 0:
        print("неверный ввод, попробуйте заново")
        return char()
    dexterity = int(input("Ловкость персонажа (от 1 до 10): "))
    if dexterity > 10 or dexterity < 0:
        print("неверный ввод, попробуйте заново")
        return char()
    intelligence = int(input("Интеллект персонажа (от 1 до 10): "))
    if intelligence > 10 or intelligence < 0:
        print("неверный ввод, попробуйте заново")
        return char()
    ch = Character(name, age, strength, dexterity, intelligence)
    return ch


def random_event(ch):
    events = [event1, event2, event3]
    return choice(events)(ch)


def main():
    ch = char()
    print(f"Имя: {ch.name}, возраст: {ch.age}, СИЛ: {ch.strength}, ЛОВ: {ch.dexterity}, ИНТ: {ch.intelligence}")
    print("-----------------------------------------------------------------------------------")
    road = int(input("Вы заблудились в лесу. Перед вами три дорожки. Куда вы пойдете? (введите номер пути): "))
    if 1 <= road <= 3:
        random_event(ch)
    else:
        print("Вы нашли еще одну тропу и просто вышли из леса.")


if __name__ == '__main__':
    main()
