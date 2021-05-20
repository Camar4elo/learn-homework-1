"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    user_answer = 0
    while user_answer != 'Хорошо':
        user_answer = input('Как дела?: ')

    
if __name__ == "__main__":
    hello_user()
