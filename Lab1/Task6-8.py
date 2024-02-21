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

