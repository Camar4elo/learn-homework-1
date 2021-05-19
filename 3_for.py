"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    all_scores_list = [
    {'school_class': '1a', 'scores': [5, 2, 5, 1, 2, 3, 4, 1, 2, 1]},
    {'school_class': '5б', 'scores': [1, 2, 2, 1, 2, 3, 3, 5, 2, 1]},
    {'school_class': '9в', 'scores': [5, 5, 5, 4, 5, 3, 4, 2, 2, 1]},
    {'school_class': '7г', 'scores': [2, 5, 5, 3, 2, 3, 4, 2, 4, 4]},
    {'school_class': '3a', 'scores': [4, 5, 1, 5, 4, 5, 5, 5, 5, 2]}
]

    total_len = 0
    total_score = 0
    for score in all_scores_list:
        total_len += len(score['scores'])
        total_score += sum(score['scores'])
    print(f'Средняя оценка по школе: {total_score / total_len}')

    for score in all_scores_list:
        class_number = score['school_class']
        average_score = sum(score['scores']) / len(score['scores'])
        print(f'Средняя оценка по классу: {class_number} {average_score}')
    
if __name__ == "__main__":
    main()
