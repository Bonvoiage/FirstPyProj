# Создайте новый проект или продолжите работу в текущем проекте
# Ваша задача:


name = '../FirstPyProj/module_7/7_3/module_7_3_old.txt'

with open(name, encoding="utf-8") as file:
    for line in file:
        print(line, end="")

# Создайте в директории проекта текстовый файл с расширением txt
# Добавьте в этот файл следующий текст
# # -*- coding: utf-8 -*-
# My soul is dark - Oh! quickly string
# The harp I yet can brook to hear;
# And let thy gentle fingers fling
# Its melting murmurs o'er mine ear.
# If in this heart a hope be dear,
# That sound shall charm it forth again:
# If in these eyes there lurk a tear,
# 'Twill flow, and cease to burn my brain.
# But bid the strain be wild and deep,
# Nor let thy notes of joy be first:
# I tell thee, minstrel, I must weep,
# Or else this heavy heart will burst;
# For it hath been by sorrow nursed,
# And ached in sleepless silence, long;
# And now 'tis doomed to know the worst,
# And break at once - or yield to song.
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with
# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Получившийся код прикрепите к заданию текстом
