# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# print(type(students))                                            # Проверил тип
students = list(students)                                          # Перевел тип в список
# print(students)                                                  # Проверил

# counter_students = int(0)                                         # Добавил переменную
# stu_list = { students[counter_students]       : sum(grades[counter_students])/len(grades[counter_students]) ,
#              students[(counter_students + 1)] : sum(grades[counter_students])/len(grades[counter_students]) ,
#              students[(counter_students + 1)] : sum(grades[counter_students])/len(grades[counter_students]) ,                             # Создал словарь
#              students[(counter_students + 1)] : sum(grades[counter_students])/len(grades[counter_students]) ,
#              students[(counter_students + 1)] : sum(grades[counter_students])/len(grades[counter_students])  }
#    по какой-то причине у меня не завелось, попробовал counter_students +=1, результат тот же, вроде логика соблюдена

stu_list = { students[0] : sum(grades[0])/len(grades[0]) ,
             students[1] : sum(grades[1])/len(grades[1]) ,
             students[2] : sum(grades[2])/len(grades[2]) ,
             students[3] : sum(grades[3])/len(grades[3]) ,
             students[4] : sum(grades[4])/len(grades[4])
}

print(stu_list)                                                    # вывел для проверки






















#
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
