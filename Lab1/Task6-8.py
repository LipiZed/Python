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

