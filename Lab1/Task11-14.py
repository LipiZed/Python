def sogl_glasn(text):
    glasn = 'аеёиоуыэюя'
    sogl = 'бвгджзйклмнпрстфхцчшщъь'
    text = text.lower()
    glasn_count = sum(1 for char in text if char in glasn)
    sogl_count = sum(1 for char in text if char in sogl)
    return sogl_count-glasn_count

def sort_by_sogl_glasn(strings):
    return sorted(strings, key=sogl_glasn)


def average_ascii_weight(text):
    total_weight = sum(ord(char) for char in text)
    return total_weight / len(text)

def quadratic_deviation(text, reference_avg_weight):
    avg_weight = average_ascii_weight(text)
    return (avg_weight - reference_avg_weight) ** 2

def sort_strings_by_deviation(strings):
    reference_avg_weight = average_ascii_weight(strings[0])
    return sorted(strings, key=lambda x: quadratic_deviation(x, reference_avg_weight))

