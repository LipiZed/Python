# Задача 1
def sogl_glasn(text):
    glasn = 'аеёиоуыэюя'
    sogl = 'бвгджзйклмнпрстфхцчшщъь'
    text = text.lower()
    glasn_count = sum(1 for char in text if char in glasn)
    sogl_count = sum(1 for char in text if char in sogl)
    return sogl_count - glasn_count


def sort_by_sogl_glasn(strings):
    return sorted(strings, key=sogl_glasn)


# Задача 4
def average_ascii_weight(text):
    total_weight = sum(ord(char) for char in text)
    return total_weight / len(text)


def quadratic_deviation(text, reference_avg_weight):
    avg_weight = average_ascii_weight(text)
    return (avg_weight - reference_avg_weight) ** 2


def sort_strings_by_deviation(strings):
    reference_avg_weight = average_ascii_weight(strings[0])
    return sorted(strings, key=lambda x: quadratic_deviation(x, reference_avg_weight))


# Задача 7

def count_sochet(text):
    glasn = 'аеёиоуыэюя'
    sogl = 'бвгджзйклмнпрстфхцчшщъь'
    count = 0
    max_count = 0
    for i in range(len(text) - 1):
        if (text[i] in glasn and text[i + 1] in sogl) or (text[i] in sogl and text[i + 1] in glasn):
            count += 1
    else:
        max_count = count
        count = 0
    return max_count

def sort_count_sochet(strings):
    return sorted(strings, key=count_sochet)

# Задача 10

def count_triple(text):
    count = 0
    max_count = 0
    for i in range(len(text) - 2):
        if (text[i] == text[i + 2]):
            count += 1
    else:
        max_count = count
        count = 0
    return max_count

def sort_count_triple(strings):
    return sorted(strings, key=count_triple)

a = int(input("Введите по какому принципу хотите сортировать список строк: "))
match a:
    case 1:
        print("Сортировка по разнице между согласными и гласными")
        print("Вводите строки, если вы хотите закончить ввод, введите пустую строку: \n")
        strings = []
        while True:
            a = input()
            if a == "":
                break
            strings.append(a)
        print(sort_by_sogl_glasn(strings))
    case 2:
        print("Сортировка в порядке увеличения квадратичного отклонения")
        print("Вводите строки, если вы хотите закончить ввод, введите пустую строку: \n")
        strings = []
        while True:
            a = input()
            if a == "":
                break
            strings.append(a)
        print(sort_strings_by_deviation(strings))
    case 3:
        print("Сортировка по сочетаниям гласная-согласная и наоборот")
        print("Вводите строки, если вы хотите закончить ввод, введите пустую строку: \n")
        strings = []
        while True:
            a = input()
            if a == "":
                break
            strings.append(a)
        print(sort_count_sochet(strings))
    case 4:
        print("Сортировка по зеркальным тройкам")
        print("Вводите строки, если вы хотите закончить ввод, введите пустую строку: \n")
        strings = []
        while True:
            a = input()
            if a == "":
                break
            strings.append(a)
        print(sort_count_triple(strings))
    case _:
        print("Такой задачи нет.")