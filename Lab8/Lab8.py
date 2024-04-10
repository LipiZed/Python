from overpy import Overpass

# Загрузка OSM-файла
api = Overpass()
result = api.parse_xml(open("7.osm", 'r', encoding="utf8").read())

# Словарь для хранения информации о школах
schools = {}

# Обработка всех элементов
for element in result.nodes:
        # Проверка тега "amenity"
        if 'amenity' in element.tags:
            # Проверка, является ли тег "school"
            if element.tags['amenity'] == 'school':
                # Извлечение информации
                school_name = element.tags['name'] if 'name' in element.tags else 'Unknown'
                address = element.tags['address'] if 'address' in element.tags else 'Unknown'
                # Добавление информации в словарь
                if school_name not in schools:
                    schools[school_name] = []
                schools[school_name].append(address)

# Сортировка по имени
sorted_schools = sorted(schools.items())

# Вывод результатов
for school_name, addresses in sorted_schools:
    print(f"{school_name}")
    for address in addresses:
        print(f"Адрес: \t- {address}")

