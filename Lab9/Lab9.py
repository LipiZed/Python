import csv
from dateparser import parse

# Загружаем данные из CSV-файла
with open("16 - 2.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Пропускаем заголовок
    next(reader, None)

    # Задаем параметры
    min_score = 60  # минимальный балл

    # Список для хранения отсортированных данных
    sorted_data = []

    for row in reader:
        # Получаем информацию из строки
        last_name, first_name, _, _, email, _, test_started, test_ended, time_spent, score, *_ = row

        # Парсим даты
        start_date = parse(test_started)
        end_date = parse(test_ended)
        if score == '-':  # Проверяем наличие дефиса
            score = 0.0
        else:
            score = float(score.replace(',', '.'))  # Заменяем запятую на точку и преобразуем во float
        # Проверяем, что даты успешно распознаны
        if start_date is not None and end_date is not None:
            # Проверяем условия
            if score != '-' and float(score) >= min_score and start_date <= parse(test_started) <= end_date:
                # Добавляем данные в список
                sorted_data.append((last_name, first_name, email, score))

    # Сортируем список по фамилии и имени
    sorted_data.sort(key=lambda x: (x[0], x[1]))

# Выводим результат
for last_name, first_name, email, score in sorted_data:
    print(f"{last_name} {first_name} : {score}")
