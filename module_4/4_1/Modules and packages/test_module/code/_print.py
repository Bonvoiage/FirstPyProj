'''
Вы по первым занятиям уже знакомы с функцией print(). Но сейчас я хочу поговорить о том, насколько эта функция мощная, если к ней применить форматированный строковые литералы, которые называются f - строкой, а еще точнее, литералом форматирования.
'''

#* Пример № 1
''' 
Форматирование даты и времени 
Форматирование чисел средствами f-строк — это обычное дело. А вы знали, что с их помощью можно ещё форматировать значения, представляющие даты и временные метки?
'''

import datetime
today = datetime.datetime.today()

# print(today)

# Вывод -> 2023-11-01 00:00:00.000000

#* Пример №2
# print(f'{today:%Y-%m-%d}')
# Вывод -> 2023-11-01

#* Пример № 3
# print(f'{today:%Y}')
# Вывод 2023

#* Пример № 4
# print(f'{today:%H:%M:%S}')

# Вывод -> 00:00:00

#* Пример № 5
# print('{:^30}'.format(f'*{today:%H:%M:%S}'))

# Вывод -> 00:00:00

#* Пример № 6
#* Имена переменных и отладка

# x = 10
# y = 25

# print(f'x = {x}, y = {y}')
# Вывод -> x = 10, y = 25

#* Пример № 7
# print(f'{x = }, {y = }')
# Вывод -> x = 10, y = 25

#* Пример № 8
# print(f'{x = :.3f}')
# Вывод -> x = 10.000

#* Пример № 9
'''
Вся сила мини-языка спецификаций форматирования. 
# F-строки поддерживают мини-язык спецификаций форматирования Python. Поэтому в модификаторы, используемые в f-строках, можно внедрить множество операций форматирования данных:
'''

# text = "hello world"

#* Центрирование текста:

# print(f"{text:^15}")
# Вывод ->'  hello world  '

#* Пример № 10
# number = 1234567890

#* Установка разделителя групп разрядов
# print(f"{number:,}")
# # 1,234,567,890

#* кстати, а вы знали?

# number = 1_000_000_000
# print(f"{number * 5}")


# number = 123

#* Добавление начальных нулей
# print(f"{number:08}")
# Вывод -> 00000123

#* Ссылки, где стоит почитать о шаблонах форматирования
# https://pythonim.ru/string/format-python?ysclid=logrreqokd677175187
# https://stavis-dev.github.io/python/functions/f-string/?ysclid=logrqouere556053735



#* Цветной вывод текста в Python

'''
Python обладает достаточным количеством инструментов, чтобы выводить текст в консоль в любом цвете. Такой вывод не требует особых навыков, реализуется в несколько строк кода и используется как для выделения важной информации, так и для придания красоты тексту.

Сделать текст цветным можно двумя способами: использовать встроенные средства языка или библиотеки. Каждый способ имеет плюсы и минусы, также существуют нюансы, касающиеся изменения цвета текста в консоли Windows.

Изменять цвет текста с помощью ANSI кодов можно разными способами, например, использоваться функции или даже написать свой класс-обёртку для ANSI.

Использовать ANSI коды просто, для этого нужно знать базовый синтаксис и сами коды. Разбор на примере кода «\033[31m\033[43m»:

\033 — обозначение того, что дальше идет какой-то управляющий цветом код;
[31m — цвет текста (красный);
[43m — цвет фона (жёлтый).
После вывода этого в консоль, далее выводимая информация будет красного цвета на жёлтом фоне. Сбросить к начальным значениям : \033[0m.

Базовые коды:

\033[0-7m — это различные эффекты, такие как подчеркивание, мигание, жирность и так далее;
\033[30-37m — коды, определяющие цвет текста (черный, красный, зелёный, жёлтый, синий, фиолетовый, сине-голубой, серый);
\033[40-47m — коды, определяющие цвет фона.
'''
#* Пример № 11

# def out_red(text):
#     print(f"\033[31m {text}")
# def out_yellow(text):
#     print(f"\033[33m {text}")
# def out_blue(text):
#     print(f"\033[34m {text}")

# out_red("Вывод красным цветом")

# out_yellow("Текст жёлтого цвета")

# out_blue("Синий текст")


# вернем цвет, который был

# print(f"\033[0m Hello world")

'''
Мы меняли только цвет текста, но можно менять и цвет фона, добавлять дополнительные стили. Например, чтобы вывести подчёркнутый текст белого цвета на синем фоне, нужно написать так:
'''

#* Пример № 12
# print('\033[4m\033[37m\033[44m{}\033[0m'.format('Python 3'))

'''
Здесь мы вывод осуществляли следующим образом:

\033[4m — подчёркнутый;
\033[37m — белая надпись;
\033[44m — синий фон;
{} — заменится на «Python 3»;
\033[0m — сброс к начальным значениям.
'''

'''
Вывод цветного текста в консоль с colorama
Colorama — самая популярная библиотека для вывода цветного текста на Python 3. Colorama позволяет использовать ANSI коды не только в Linux, но и в Windows.

Использование функций и методов библиотеки упрощает написание кода и делает более простым для поддержки. Больше не нужно запоминать или копировать ANSI коды. Команды настолько просты и интуитивно понятны, что с задачей справиться даже обычный пользователь.

Использование сторонней библиотеки, такой как colorama, не приводит к каким-то негативным эффектам. Перед использованием библиотеки colorama, её следует установить с помощью команды в консоле pip install colorama.
'''

#* Пример № 13
#* Пример использования библиотеки colorama

# import colorama
# from colorama import Fore, Back, Style
# colorama.init()

# print(Fore.RED + 'Красный текст')
# print(Back.BLUE + 'Синий фон')

# print(Style.RESET_ALL)
# print('Снова обычный текст')
