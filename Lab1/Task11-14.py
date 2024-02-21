def sogl_glasn(text):
    glasn = 'аеёиоуыэюя'
    sogl = 'бвгджзйклмнпрстфхцчшщъь'
    text = text.lower()
    glasn_count = sum(1 for char in text if char in glasn)
    sogl_count = sum(1 for char in text if char in sogl)
    return sogl_count-glasn_count

def sort_by_sogl_glasn(strings):
    return sorted(strings, key=sogl_glasn)

