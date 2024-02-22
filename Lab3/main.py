class Point:
    def __init__(self, x, y):
        self.x = x  # Координата x точки на плоскости
        self.y = y  # Координата y точки на плоскости


class Pentagon:
    def __init__(self, identifier, vertices):
        self.identifier = identifier  # Идентификатор пятиугольника
        self.vertices = vertices  # Список вершин пятиугольника

    def area(self):
        # Формула площади пятиугольника по координатам вершин
        x = [v.x for v in self.vertices]
        y = [v.y for v in self.vertices]
        return 0.5 * abs(sum(x[i] * (y[i] - y[i - 1]) for i in range(5)) + x[4] * (y[0] - y[3]) - x[0] * (y[4] - y[1]))


    def compare(self, other):
            return self.area() - other.area()  # Сравнение площади
    def is_intersect(self, triangle):
        if not isinstance(triangle, Triangle):
            raise ValueError("Проверка только между сущностями Пятиугольника и Треугольника")

        # Проверяем пересечение каждой стороны пятиугольника с каждой стороной треугольника
        for i in range(5):
            p1 = self.vertices[i]  # Текущая вершина пятиугольника
            p2 = self.vertices[(i + 1) % 5]  # Следующая вершина пятиугольника

            for j in range(3):
                t1 = triangle.vertices[j]  # Текущая вершина треугольника
                t2 = triangle.vertices[(j + 1) % 3]  # Следующая вершина треугольника

                if self.do_intersect(p1, p2, t1, t2):  # Проверяем пересечение отрезков
                    return True

        return False

    @staticmethod
    def do_intersect(p1, q1, p2, q2):
        def orientation(p, q, r):
            val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and Pentagon.on_segment(p1, p2, q1):
            return True

        if o2 == 0 and Pentagon.on_segment(p1, q2, q1):
            return True

        if o3 == 0 and Pentagon.on_segment(p2, p1, q2):
            return True

        if o4 == 0 and Pentagon.on_segment(p2, q1, q2):
            return True

        return False

    @staticmethod
    def on_segment(p, q, r):
        return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)


class Triangle:
    def __init__(self, identifier, vertices):
        self.identifier = identifier  # Идентификатор треугольника
        self.vertices = vertices  # Список вершин треугольника

    def area(self):
        # Формула площади треугольника по координатам вершин
        x = [v.x for v in self.vertices]
        y = [v.y for v in self.vertices]
        return 0.5 * abs(x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))

    def compare(self, other):
        return self.area() - other.area()  # Сравнение площади

    def is_intersect(self, pentagon):
        if not isinstance(pentagon, Pentagon):
            raise ValueError("Проверка пересечения поддерживается только между объектами Треугольник и Пятиугольник")

        # Проверяем пересечение каждой стороны треугольника с каждой стороной пятиугольника
        for i in range(3):
            t1 = self.vertices[i]
            t2 = self.vertices[(i + 1) % 3]

            for j in range(5):
                p1 = pentagon.vertices[j]
                p2 = pentagon.vertices[(j + 1) % 5]

                if Pentagon.do_intersect(p1, p2, t1, t2):
                    return True

        return False

# Создаем объекты пятиугольника и треугольника
pentagon_vertices = [Point(0, 0), Point(3, 0), Point(5, 2), Point(2, 4), Point(1, 2)]
triangle_vertices = [Point(1, 1), Point(2, 0), Point(3, 1)]
pentagon = Pentagon("pentagon1", pentagon_vertices)
triangle = Triangle("triangle1", triangle_vertices)

# Проверяем пересечение
if pentagon.is_intersect(triangle):
    print("Пятиугольник пересекается с треугольником.")
else:
    print("Пятиугольник не пересекается с треугольником.")

if triangle.is_intersect(pentagon):
    print("Треугольник пересекается с пятиугольником.")
else:
    print("Треугольник не пересекается с пятиугольником.")

print(pentagon.compare(triangle))