# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

numbers_len = len(numbers)

for i in range (numbers_len):
    is_prime = 0
    for j in range (2, numbers[i]-1):
        if is_prime == 1:
            break
        elif numbers[i] % j == 0:
            is_prime += 1
    if is_prime == True:                    #Проверка, если порядковый номер в списке Numbers - не простой, тогда выполняется следующее действие: Добавить в список not_primes
        not_primes.append(numbers[i])
    elif is_prime == False:
        primes.append(numbers[i])           #Проверка, если порядковый номер в списке Numbers - простой, тогда выполняется следующее действие: Добавить в список primes
    else:
        print("Who care, just chill")
print(f"Primes: {primes}")  
print(f"Not primes: {not_primes}")