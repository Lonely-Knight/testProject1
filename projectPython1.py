import re

# функция по добавлению нулей слева от числа
def convert_number(match):
    number = match.group()
    parts = number.split('\\')
    # добавляет нули в левой части от backslash
    left_part = parts[0].zfill(4)
    # добавляет нули в правой части от backslash
    right_part = parts[1].zfill(5)
    # печать измененного номера
    print(f"{left_part}\\{right_part}")

# поиск искомых данных по regex и отправка в функцию для исправления
def format_numbers(input_str):
    pattern = r'\d{2,4}\\\d{2,5}'
    re.sub(pattern, convert_number, input_string)


# Входные данные: Адрес 5467\456. Номер 405\549
input_string = input("Введите входные данные: ")
# input_string = "Адрес 5467\\456. Номер 405\\549"
format_numbers(input_string)
