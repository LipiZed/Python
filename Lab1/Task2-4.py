def count_russian_chars(text):
  count = 0
  for char in text:
    if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
      count += 1
  return count

def latin_palindrom(text):
    text = text.lower()
    text = "".join(char for char in text if char.isalpha() and char.islower() and not char.isalpha())
    return text == text[::-1]




