'''
Словари в Python – это изменяемые отображения ссылок на объекты, доступные по ключу. Словари представляют собой структуры данных, в которых уникальные ключи отображают значения. Ключ и значение разделяются двоеточием, пары ключ-значения отделяются запятыми, а словарь целиком ограничивается фигурными скобками {}. Ниже приведены три словаря, содержащие сведения о населении пяти крупнейших городов Германии, список покупок и оценки студентов.
'''

population = {
              'Берлин': 3748148, 
              'Гамбург': 1822445, 
              'Мюнхен': 1471508, 
              'Кёльн': 1085664, 
              'Франкфурт': 753056 
             }

products = {
            'стол': 120, 
            'стул': 40, 
            'лампа': 14, 
            'кровать': 250, 
            'матрац': 100
           }

grades = {
          'Алла': 9.5, 
          'Эдуард': 10, 
          'Виктор': 3.5, 
          'Елена': 6.5, 
          'Ирина': 7.5
         }


'''
Создание словаря при помощи dict()
Кроме прямого описания, словари также можно создавать с помощью встроенной функции dict(). Эта функция принимает любое количество именованных аргументов.
'''
# students_ages = dict(
#                      Алла = 27, 
#                      Виктория = 38, 
#                      Ангелина = 17, 
#                      Михаил = 40
#                     )
# print(students_ages)

'''
Методы можно комбинировать:
'''
# students_ages = dict(
#                      {
#                       'Алла': 27, 
#                       'Виктория': 38
#                      }, 
#                       Ангелина = 17, 
#                       Михаил = 40
#                     )
# print(students_ages)


'''
Другой вариант – использовать список кортежей. Каждый кортеж должен содержать два объекта: ключ и значение.
'''
# students_ages = dict(
#                      [
#                       ('Алла', 27), 
#                       ('Виктория', 38), 
#                       ('Ангелина', 17), 
#                       ('Михаил', 40)
#                      ]
#                     )
# print(students_ages)


'''
Можно создать словарь, используя два списка. Вначале строим итератор кортежей с помощью функции zip(). Затем используем ту же функцию dict() для построения словаря.
'''
# students = [
#             'Алла', 
#             'Виктория', 
#             'Ангелина', 
#             'Михаил'
#             ]
# ages = [27, 38, 17, 40]
# students_ages = dict(zip(students, ages))
# print(students_ages)


'''
Для доступа к значениям словаря мы не можем использовать числовой индекс (как в случае со списками или кортежами). Однако схема извлечения значения похожа на индексацию: вместо числа в квадратные скобки подставляется ключ. При попытке получить доступ к значению с помощью несуществующего ключа будет вызвана ошибка KeyError.

Чтобы избежать получения исключения с несуществующими ключами, можно воспользоваться методом dict.get(key[, default]). Этот метод возвращает значение для ключа, если ключ находится в словаре, иначе возвращает значение по умолчанию default. Если значение по умолчанию не задано, метод возвращает None (но никогда не возвращает исключение).
'''
# print(population['Мюнхен'])

# print(population[1])

# print(population['Штудгарт'])

# print(population.get('Мюнхен'))

# print(population.get('Штудгарт'))

# print(population.get('Штудгарт', 'Не найдено'))


'''
Добавить одиночный элемент в словарь можно следующим образом:
'''
# print(products)

# products['подушка'] = 10
# print(products)

'''
Для добавления нескольких элементов одновременно можно применять метод dict.update([other]). Он обновляет словарь парами ключ-значение из other, перезаписывая существующие ключи.  Метод update() может принимать в качестве аргумента не только словарь, но и список кортежей или именованные аргументы.
'''
# print(products)
products.update(
                {
                 'полка': 70, 
                 'диван': 300
                }
               )
# print(products)

grades.update(
              Виолета = 5.5, 
              Марк = 6.5, 
              Павел = 8
             )
# print(grades)

population.update(
                  [
                   ('Штудгарт', 632743), 
                   ('Дюссельдорф', 617280)
                  ]
                 )
# print(population)

'''
Изменим значение элемента, обратившись к ключу с помощью квадратных скобок ([]). Для изменения нескольких значений сразу есть метод .update(). Он перезаписывает существующие ключи.

Увеличим цену дивана на 100 единиц и изменим оценки двух студентов.
'''
# print(products)

# products['диван'] = 400
# print(products)

# print(grades)

# grades.update(
#               {
#                'Виктор': 2.5, 
#                'Виолета': 6
#               }
#              )
# print(grades)

'''
Для удаления элемента из словаря можно использовать либо del dict[key], либо dict.pop(key[, default]). В первом случае из словаря удаляется соответствующая пара. Или, если такого ключа нет, возвращается KeyError.
Метод dict.pop(key[, default]) удаляет из словаря элемент с заданным ключом и возвращает его значение. Если ключ отсутствует, метод возвращает значение default . Если значение default не задано и ключа не существует, метод pop() вызовет исключение KeyError.
'''
# print(population)

# del population['Дрезден']

# del population['Дюссельдорф']
# print(population)


# print(population)

# population.pop('Штудгарт')

# print(population)

# print(population.pop('Дрезден', 'Значение не найдено'))

# print(population.pop('Париж', 'Значение не найдено'))


'''
Чтобы проверить, существует ли ключ в словаре, достаточно воспользоваться операторами принадлежности:
'''
# print(population)

# print('Нью-Йорк' in population)

# print('Мюнхен' in population)

# print('Париж' not in population)

# print('Мюнхен' not in population)


'''
Метод setdefault() в Python является встроенным методом словаря и используется для возврата значения ключа, если он уже существует в словаре. Если ключ не существует, метод устанавливает значение по умолчанию и возвращает его.
'''
# person = {
#           'name': 'John',
#           'age': 30,
#          }

# print(person)
# print(person.setdefault('City'))
# print(person)

'''
Чтобы скопировать словарь, можно использовать метод словаря copy(). Этот метод возвращает поверхностную копию словаря. Мы должны быть осторожны с такими копиями: если словарь содержит списки, кортежи или множества, то в созданной копии будут только ссылки на объекты из оригинала.
'''
# students = {
#             'Иван': 173, 
#             'Лев': 184, 
#             'Андрей': 168
#            }
# students_2 = students.copy()  # поверхностная копия
# students_2['Лев'] = 180
# print(students)

# print(students_2)

# students_weights = {
#                     'Иван': [173, 70], 
#                     'Лев': [184, 80], 
#                     'Андрей': [168, 57]
#                    }
# students_weights_2 = students_weights.copy()
# students_weights_2['Лев'][0] = 180
# print(students_weights)
# print(students_weights_2)

'''
Изменение в спискеstudents_2 затронуло список students, так как список, содержащий вес и рост, содержит ссылки, а не дубликаты. Чтобы избежать этой проблемы, создадим глубокую копию, используя функцию copy.deepcopy(x):
'''
# import copy
# students_weights = {
#                     'Иван': [173, 70], 
#                     'Лев': [184, 80], 
#                     'Андрей': [168, 57]
#                     }
# students_weights_2 = copy.deepcopy(students_weights)
# students_weights_2['Лев'][0] = 180
# print(students_weights)

# print(students_weights_2)

'''
При использовании глубокого копирования создается полностью независимая копия.

Важно помнить, что оператор = не создаёт копию словаря. Он присваивает другое имя, но относящееся к тому же словарю, т. е. любое изменение нового словаря отражается на исходном.
'''
# fruits = {'апельсины': 50, 'яблоки': 65, 'авокадо': 160, 'персики': 75}
# fruits_2 = fruits
# fruits_2.pop('апельсины')

# print(fruits)


'''
Чтобы выяснить сколько пар ключ-значение содержится в словаре, достаточно воспользоваться функцией len():
'''
# print(population)

# print(len(population))


'''
Чтобы перебрать все ключи, достаточно провести итерацию по элементам объекта словаря:
'''
# for city in population:
#     print(city)


'''
Вычислим сколько людей проживает в пяти крупнейших городах Германии. Применим метод dict.values(), возвращающий список значений словаря:
'''
# print(population)

# total_people = 0
# for number in population.values():
#     total_people += number

# print(total_people)


'''
В случае, если нужно работать с ключами и значениями одновременно, обратимся к методу dict.items(), возвращающему пары ключ-значение в виде списка кортежей.
'''
# print(grades)
# min_grade = 10
# min_student = ''
# for student, grade in grades.items():
#     if grade < min_grade:
#             min_student = student
#             min_grade = grade

# print(min_student)


'''
Цикл for удобен, но сейчас попробуем более эффективный и быстрый способ – генератор словарей. Синтаксис выглядит так: {key: value for vars in iterable}

Отфильтруем товары из словаря products по цене ниже 100, используя как цикл for, так и генератор словарей.
'''
# print(products)

# products_low = {}
# for product, value in products.items():
#     if value < 100:
#             products_low.update({product: value})

# print(products_low)

# products_low = {product: value for product, value in products.items() if value < 100}
# print(products_low)


'''
Вложенные словари – это словари, содержащие другие словари. Мы можем создать вложенный словарь так же, как мы создаем обычный словарь, используя фигурные скобки.

Следующий вложенный словарь содержит информацию о пяти известных произведениях искусства. Как можно заметить, значениями словаря являются другие словари.
'''
# from pprint import pprint

# works_of_art = {
#                 'Звездная_ночь': 
#                 {
#                  'автор': 'Ван Гог', 
#                  'год': 1889, 
#                  'стиль': 'пост-импрессионизм'
#                 },
#                 'Рождение_Венеры': 
#                 {
#                  'автор': 'Сандро Ботичелли', 
#                  'год': 1480, 
#                  'стиль': 'ренессанс'
#                 },
#                 'Герника': 
#                 {
#                   'автор': 'Пабло Пикассо', 
#                   'год': 1937, 
#                   'стиль': 'кубизм'
#                 },
#                 'Американская_готика': 
#                 {
#                  'автор': 'Грант Вуд', 
#                  'год': 1930, 
#                  'стиль': 'регионализм'
#                 },
#                 'Поцелуй': 
#                 {
#                  'автор': 'Густав Климт', 
#                  'год': 1908, 
#                  'стиль': 'новое искусство'
#                 }
#                }


'''
Создадим вложенный словарь, используя dict(), передавая пары ключ-значение в качестве именованных аргументов.
'''
# works_of_art = dict(
#                     Звездная_ночь = 
#                                     {
#                                      'автор': 'Ван Гог', 
#                                      'год': 1889, 
#                                      'стиль': 'пост-импрессионизм'
#                                     },
#                     Рождение_Венеры = 
#                                     {
#                                      'автор': 'Сандро Ботичелли', 
#                                      'год': 1480, 
#                                      'стиль': 'ренессанс'
#                                     },
#                     Герника =
#                                     {
#                                      'автор': 'Пабло Пикассо', 
#                                      'год': 1937, 
#                                      'стиль': 'кубизм'
#                                     },
#                     Американская_готика = 
#                                     {
#                                      'автор': 'Грант Вод', 
#                                      'год': 1930, 
#                                      'стиль': 'регионализм'
#                                     },
#                     Поцелуй = 
#                                     {
#                                      'автор': 'Густав Климт', 
#                                      'год': 1908, 
#                                      'стиль': 'новое искусство'
#                                     }
#                    )

# pprint(works_of_art)


'''
Для доступа к элементам во вложенном словаре указываем ключи, используя несколько квадратных скобок ([ ][ ]).
'''

# print(works_of_art['Герника']['автор'])

# print(works_of_art['Американская_готика']['стиль'])




