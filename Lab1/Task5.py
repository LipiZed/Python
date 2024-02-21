import re
def find_dates(text):
    pattern = r'\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}'
    dates = re.findall(pattern, text)
    return dates

