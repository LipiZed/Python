import re


def is_number(string):
    pattern = r'\b^(\+7|8)-\d{3}\-\d{3}\-\d{2}\-\d{2}\b'
    if re.match(pattern, string):
        return True
    else:
        return False

print(is_number('8-918-659-45-30'))