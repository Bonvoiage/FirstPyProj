def check_winner():
    for row in range(3):
        if area[row][0] == area[row][1] == area[row][2] != area_symbol:     # Если, строка, столбец 1, столбец 2, столбец 3 не равны area_symbol и равны между собой, то
            return area[row][0]                                                   # Возвращаем значение из 1 столбца заданной строчки
    for col in range(3):                                                    
        if area[0][col] == area[1][col] == area[2][col] != area_symbol:     # Если, столбец, строка 1, строка 2, строка 3 не равны area_symbol и равны между собой, то
            return area[0][col]                                             # Возвращаем значение из 1 строчки заданного столбца
    if area[0][0] == area[1][1] == area[2][2] != area_symbol:               # Проверка диагоналей, после проверки - возвращает символ который стоит в ячейке 0 0
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0] != area_symbol:               # Проверка диагоналей, после проверки - возвращает символ который стоит в ячейке 0 2
        return area[0][2]
    return noone_win

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
x = "X"
o = "O"
noone_win = "Draw"
turn_1_player = 1
turn_2_player = 1
current_turn = int(turn_1_player + turn_2_player) -1

print("Lets start")
print()
draw_area()
for i in range (1, 50):
    if check_winner() == x:
        print("Победил 1 игрок")
        break
    if check_winner() == o:
        print("Победил 2 игрок")
        break
    if check_winner() == noone_win and current_turn == 11:                                     # Прерывание, когда определился победитель
        print("Победителя нет.")
        break
    elif player_turn % 2 == 0:                              # Логика Первого игрока
        print()
        print(f"Ход {current_turn}")
        print(f"Ход игрока 1 со знаком '{x}' ")               # Обозначение хода
        print()
        row = int(input("Введите Строку: "))                    # Ввод строки
        row -= 1                                                # Счет идет с 0, поэтому вычитаем из строки -1
        col = int(input("Введите Столбец: "))                   # Ввод столбца
        col -= 1                                                # Счет идет с 0, поэтому вычитаем из столбца -1
        print()
        if area[row][col] != (area_symbol):                     # Проверка на то, что была задействованна правильная ячейка
            print("Вы не можете перезаписать чужой ход")
            player_turn -= 1                                    # Возвращаем ход игроку, который совершил не верный ход.
            turn_1_player = -1                                              # Возвращаем значение i к моменту, когда игрок ошибся.
        elif area[row][col] == (area_symbol):                   # Проверка пройдена
            area[row][col] = (x)                                # Записываем в ячейку "х" первого игрока
        player_turn += 1                                        # Передаем ход другому
        draw_area()
    elif player_turn % 2 == 1:                              # Логика второго игрока
        print()
        print(f"Ход {current_turn}")
        print(f"Ход игрока 2 со знаком '{o}' ")              # Обозначение хода
        print()
        row = int(input("Введите Строку: "))                    # Ввод строки
        row -= 1                                                # Счет идет с 0, поэтому вычитаем из строки -1
        col = int(input("Введите Столбец: "))                   # Ввод столбца
        col -= 1                                                # Счет идет с 0, поэтому вычитаем из столбца -1
        print()
        if area[row][col] != (area_symbol):
            print("Вы не можете перезаписать чужой ход")
            player_turn -= 1
            turn_2_player = -1
        elif area[row][col] == (area_symbol):
            area[row][col] = (o)
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