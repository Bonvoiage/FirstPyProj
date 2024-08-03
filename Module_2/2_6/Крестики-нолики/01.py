def draw_area():    
  for i in area:
    print(*i)
area_symbol = "*"                                   # Символ игрового поля
area = [                                            # Игровое поле
    [area_symbol, area_symbol, area_symbol], 
    [area_symbol, area_symbol, area_symbol], 
    [area_symbol, area_symbol, area_symbol]
    ]   
import random
player_turn = random.choice([1, 2])                     #Изначально стоит так, что ход игрока подвержен рандому, от 1 до 2
winner = 0
x = "x"
o = "o"

print("Lets start")
print()
draw_area()

for i in range (0, 9):
    if winner == 1 or i == 9:                                     # Прерывание, когда определился победитель
        if player_turn % 2 == 0:
            print("Победил 1 игрок")
        if player_turn % 2 == 1:
            print("Победил 2 игрок")
        if i == 9:
            print("Победителя нет.")
        break
    elif player_turn % 2 == 0:                              # Логика Первого игрока
        print(f"Ход игрока 1 со знаком '{x}' ")                            # Обозначение хода
        row = int(input("Введите Строку: "))                    # Ввод строки
        row -= 1                                                # Счет идет с 0, поэтому вычитаем из строки -1
        col = int(input("Введите Столбец: "))                   # Ввод столбца
        col -= 1                                                # Счет идет с 0, поэтому вычитаем из столбца -1
        if area[col][row] != (area_symbol):                             # Проверка на то, что была задействованна правильная ячейка
            print("Вы не можете перезаписать чужой ход")
            player_turn -= 1                                    # Возвращаем ход игроку, который совершил не верный ход.
            i -= 1                                              # Возвращаем значение i к моменту, когда игрок ошибся.
        elif area[col][row] == (area_symbol):                           # Проверка пройдена
            area[col][row] = (x)                              # Записываем в ячейку "х" первого игрока
        player_turn += 1                                        # Передаем ход другому
        draw_area()
    elif player_turn % 2 == 1:                              # Логика второго игрока
        print(f"Ход игрока 2 со знаком '{o}' ")                            # Обозначение хода
        row = int(input("Введите Строку: "))                    # Ввод строки
        row -= 1                                                # Счет идет с 0, поэтому вычитаем из строки -1
        col = int(input("Введите Столбец: "))                   # Ввод столбца
        col -= 1                                                # Счет идет с 0, поэтому вычитаем из столбца -1
        if area[col][row] != (area_symbol):
            print("Вы не можете перезаписать чужой ход")
            player_turn -= 1
            i -= 1
        elif area[col][row] == (area_symbol):
            area[col][row] = (o)
        player_turn += 1
        draw_area()




























# row = int(input("Введите Строку: ")) 
# row -= 1
# col = int(input("Введите Столбец: "))
# col -= 1
# input_turn = int(input("Введите 1 для х и 0 для о: "))
# if input_turn == 0:
#   area[col][row] = ("x")
# elif input_turn == 1:
#   area[col][row] = ("x")