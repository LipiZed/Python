import re


def count_russian_chars(text):
  count = 0
  for char in text:
    if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
      count += 1
  return count

def latin_palindrom(text):
    text = ''.join(char for char in text if not char.isalpha() or char.encode("utf-8").isascii())
    input_string = text.lower().replace(" ", "")
    return input_string == input_string[::-1]

def find_dates(text):
    date_regex = r"\d{1,2}\.\d{1,2}\.\d{4}"
    return re.findall(date_regex, text)

a = int(input("Введите номер задачи которую хотите решать: "))
match a:
    case 2:
        text = input("Введите строку на подсчет русских символов: ")
        print(count_russian_chars(text))
    case 3:
        text = input("Введите строку на проверку палиндлрома латинских букв: ")
        print(latin_palindrom(text))
    case 4:
        text = input("Введите сроку на поиск дат в формате дд.мм.гг: ")
        print(find_dates(text))
    case _:
        print("Такой задачи нет.")

