def count_russian_chars(text):
  count = 0
  for char in text:
    if char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
      count += 1
  return count




