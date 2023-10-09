# Функция для проверки, находится ли точка на шахматной доске 8x8
def is_valid_position(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

# Функция для определения цвета поля по его координатам
def is_same_color(x1, y1, x2, y2):
    return (x1 + y1) % 2 == (x2 + y2) % 2

# Функция для определения, угрожает ли фигура полю (x1, y1) с фигурой (x2, y2)
def is_threatening(x1, y1, x2, y2, piece):
    if piece == "ферзь":
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    elif piece == "ладья":
        return x1 == x2 or y1 == y2
    elif piece == "слон":
        return abs(x1 - x2) == abs(y1 - y2)
    
    elif piece == "конь":
        return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
    else:
        return False

# Функция для определения, можно ли с поля (x1, y1) одним ходом попасть на поле (x2, y2)
def can_move_in_one_move(x1, y1, x2, y2, piece):
    if piece == "ферзь":
        return is_threatening(x1, y1, x2, y2, piece)
    elif piece == "ладья":
        return x1 == x2 or y1 == y2
    elif piece == "слон":
        return abs(x1 - x2) == abs(y1 - y2)
    elif piece == "конь":
        return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
    else:
        return False

# Ввод координат и выбор фигуры пользователем
x1 = int(input("Введите номер вертикали (1-8) для поля (k, l): "))
y1 = int(input("Введите номер горизонтали (1-8) для поля (k, l): "))
x2 = int(input("Введите номер вертикали (1-8) для поля (m, n): "))
y2 = int(input("Введите номер горизонтали (1-8) для поля (m, n): "))
piece = input("Введите фигуру (ферзь, ладья, слон, конь): ")

# Проверка на валидность введенных данных
if not (is_valid_position(x1, y1) and is_valid_position(x2, y2)):
    print("Ошибка: Введенные координаты находятся за пределами доски.")
else:
    # Проверка на цвет поля
    if is_same_color(x1, y1, x2, y2):
        print("Поля (k, l) и (m, n) одного цвета.")
    else:
        print("Поля (k, l) и (m, n) разных цветов.")

    # Проверка на угрозу
    if is_threatening(x1, y1, x2, y2, piece):
        print(f"{piece.capitalize()} угрожает полю ({x2}, {y2}).")
    else:
        print(f"{piece.capitalize()} не угрожает полю ({x2}, {y2}).")

    # Проверка на возможность перемещения
    if can_move_in_one_move(x1, y1, x2, y2, piece):
        print(f"{piece.capitalize()} может попасть на поле ({x2}, {y2}) за один ход.")
    else:
        print(f"{piece.capitalize()} не может попасть на поле ({x2}, {y2}) за один ход.")
        # Попробуем определить два хода, если возможно
        for i in range(1, 9):
            for j in range(1, 9):
                if can_move_in_one_move(x1, y1, i, j, piece) and can_move_in_one_move(i, j, x2, y2, piece):
                    print(f"Два хода: ({x1}, {y1}) -> ({i}, {j}) -> ({x2}, {y2}).")
                    break
