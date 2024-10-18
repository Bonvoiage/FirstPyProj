class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    def __init__(self, info, args):
        self.args = args
        self.info = info
        

def f1(a, b):
    if b == 0:  
        raise ProcessingException("Деление на ноль невозможно, Процесс не стабилен, ви-у-у", {"a": a, "b": b})
    return a / b

# print(f1(10, 0))

try:
    print(f1(10, 0))
except ProcessingException as exc:
    print(f"Исключение '{exc.info}'. Его параметры: '{exc.args}'")
          


# Цель задания:
# 	Освоить механизмы создания и обработки исключений в Python.
# Научиться создавать собственные исключения, наследуя классы от Exception. Попрактиковаться в передаче исключений дальше по стеку вызовов.
# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception. Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте.
# Комментарии к заданию:
# Важно понять разницу между обработкой исключений (блок try/except) и их генерацией (оператор raise).
# Дополнительно: попробуйте использовать блоки finally или else для дополнительных действий при обработке исключений.
# Обратите внимание на то, как исключения передаются по стеку вызовов и как это можно использовать для стратегии обработки ошибок в сложных программах.
# Важно!! Для передачи обработанных исключений в вызвавшую функцию, нужно вызывать raise