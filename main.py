from names import *
import random

class NameGenerator:
    def __init__(self):
        # список возможных имен
        self.__first_names = first_names
        # список возможных отчеств
        self.__middle_names = middle_names
        # список возможных фамилий
        self.__last_names = last_names

    # метод для генерации случайного имени
    def __generate_first_name(self):
        return random.choice(self.__first_names)

    # метод для генерации случайного отчества
    def __generate_middle_name(self):
        return random.choice(self.__middle_names)

    # метод для генерации случайной фамилии
    def __generate_last_name(self):
        return random.choice(self.__last_names)

    # метод для генерации случайного полного имени
    def get_full_name(self):
        first_name = self.__generate_first_name()
        middle_name = self.__generate_middle_name()
        last_name = self.__generate_last_name()

        # возвращаем словарь с ключами 'first_name', 'middle_name' и 'last_name'
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}

while True:
    # создаём объект NameGenerator
    name_generator = NameGenerator()

    # получаем случайное полное имя
    full_name = name_generator.get_full_name()

    # извлекаем имя, отчество и фамилию из словаря
    first_name = full_name["first_name"]
    middle_name = full_name["middle_name"]
    last_name = full_name["last_name"]

    # выводим на экран полученное полное имя
    print("Имя:", first_name)
    print("Отчество:", middle_name)
    print("Фамилия:", last_name)
