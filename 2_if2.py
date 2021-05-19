"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string_1, string_2):
    if type(string_1) == str and type(string_2) == str:
        if string_1 == string_2:
            return 1
        elif string_1 != string_2 and string_2 == 'learn':
            return 3
        elif string_1 != string_2 and len(string_1) > len(string_2):
            return 2
    else:
        return 0
    
if __name__ == "__main__":
    count = 0
    while count <= 5 :
        string_1 = input('Введите строку 1: ')
        string_2 = input('Введите строку 2: ')
        print(main(string_1, string_2))
        count += 1
