def find_max_float(text):
    numbers = []
    current_number = ''
    for char in text:
        if char.isdigit() or char == '.' or (char == '-' and current_number == ''):
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''
    if current_number:
        numbers.append(float(current_number))
    if numbers:
        return max(numbers)
    else:
        return None


def find_min_rational(text):
    numbers = []
    current_number = ''
    for char in text:
        if char.isdigit() or char == '.' or (char == '-' and current_number == '') or char == '/':
            current_number += char
        elif current_number:
            numbers.append(current_number)
            current_number = ''
    if current_number:
        numbers.append(current_number)
    rational_numbers = []
    for num in numbers:
        if '/' in num:
            parts = num.split('/')
            rational_numbers.append(float(parts[0]) / float(parts[1]))
        elif '.' in num:
            rational_numbers.append(float(num))
    if rational_numbers:
        return min(rational_numbers)
    else:
        return None


def max_digits_in_a_row(text):
    numbers = []
    current_count = 0
    text = text + " "
    for char in text:
        if char.isnumeric():
            current_count = current_count + 1
        elif current_count != 0:
            numbers.append(current_count)
            current_count = 0
    return max(numbers)

a = int(input("Введите номер задачи которую хотите решать: "))
match a:
    case 6:
        text = input("Введите строку на поиск максимального вещественного: ")
        print(find_max_float(text))
    case 7:
        text = input("Введите строку на поиск минимального реционального: ")
        print(find_min_rational(text))
    case 8:
        text = input("Введите сроку на поиск макс кол-ва последовательных цифр")
        print(max_digits_in_a_row(text))
    case _:
        print("Такой задачи нет.")

