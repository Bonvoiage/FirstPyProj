#Домашняя работа по уроку "Пространство имен."



def test_function():
    print('Я в области видимости функции test_function')

    def inner_function():
        print('Я в области видимости функции inner_function')

    inner_function()


test_function() 






#Домашнее задание по уроку "Пространство имен"

# Создайте новый проект в PyCharm  --  X
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function, функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
