# # Домашняя работа по уроку "Способы вызова функции"


def e_mail_checker(e_mail_input):                                           # Логика проверки E-mail на наличие @ и ".com", ".ru", ".net"
    at_checker = "@"                                                        # Переменная для строки @
    com_checker = [".com", ".ru", ".net"]                                   # Список с переменными для проверки 
    result = 3                                                              # Стандартный результат проверки
    for i in com_checker:                                                   # Логика проверки из списка com_checker
        if at_checker in e_mail_input and i in e_mail_input:                # Проверяю, есть ли @ и значения из списка [".com", ".ru", ".net"] в операторе, для которого выполняется функция
            result = 3
            break                                                           # Если прошел проверку - прерываю for
        elif at_checker not in e_mail_input or i not in e_mail_input:       # Если нет @ или значений из списка, то присваиваю новое значение переменной и цикл проверки повторяется
            result = 2
    return result                                                           # Возвращаю результат

# test_e_mail_checker = e_mail_checker("university.help@gmail.com")
# print(test_e_mail_checker)

def send_email (message, recipient, *, sender = "university.help@gmail.com"):   # Логика фукнции отправки сообщений
    mail_passed = 0                                                             # Назначаю переменную (мог сделать ее со значеием, и в конце возвращать ее, но для того, чтобы не запутаться, изменял переменную в ходе)

    if e_mail_checker(sender) == 2:                                             # Проверить отправителя, если отправитель с ошибкой, то вернуть функцию
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return 
    elif recipient == sender:                                                   # При одинаковых значениях отправителя и получателя - переменная принимает значение 1
        mail_passed = 1
    elif e_mail_checker(recipient) == 2 and e_mail_checker(sender) == 3:        # Если фунцкия проверки "отправителя" и проверки "получателя" вернула значение 2 - то присваиваю переменной 2
        mail_passed = 2
    elif e_mail_checker(recipient) and e_mail_checker(sender) == 3:             # Если фунцкия проверки "отправителя" и проверки "получателя" вернула значение 3 - то присваиваю переменной 3
        mail_passed = 3 

    match mail_passed:                                                          # Тут в зависимости от назначения переменной выбирается что возвращать
        case 1:                                                                 # Отправитель = получатель
            mail_passed = "Вы не можете отослать сообщение себе:"
            print(mail_passed)
            return mail_passed
        case 2:                                                                 # Ошибка, либо нет @, либо ".com", ".ru", ".net"
            mail_passed = (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            print(mail_passed)
            return mail_passed
        case 3:                                                                 # Тут использую проверку, т.к. проверку на корректность e-mail пройдена, и e-mail не повторяется
            if sender != "university.help@gmail.com":                           # Если не равно дефолтному значению то
                mail_passed = (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Сообщение отправлено с адреса: {sender} на адрес {recipient}")
                print(mail_passed)
                return mail_passed
            else:                                                               # Если равно дефолту - то
                mail_passed = (f"Сообщение отправлено с адреса: {sender} на адрес {recipient}")
                print(mail_passed)
                return mail_passed



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')



# #Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

# Пример результата выполнения программы:
# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!

# Примечания:
# Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
# Именованные аргументы всегда идут после позиционных.
