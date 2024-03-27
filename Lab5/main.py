import re


def is_number(string):
    is_correct(string)
    pattern = r'^(\+7|8)-?(\(\d{3}\)|\d{3})-\d{3}-\d{2}-\d{2}$'
    if re.match(pattern, string):
        return True
    else:
        return False

def is_correct(string):
    if len(string) < 15:
        raise Exception("Это не телефон")
    return string

try:
    print(is_number('8-918-659-45-'))
except Exception:
    print("Номер некорректный, минимальная длина номера - 15 символов")