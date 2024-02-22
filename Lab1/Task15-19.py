# Задача 15
def count_after_max(list):
    a = max(list)
    index = list.index(a)
    count = 0
    for i in range(index + 1, len(list)):
        count += 1
    return count


# Задача 16
def before_min_in_the_end(list):
    index = list.index(min(list))
    result_list = list[index:]
    mins_list = list[:index]
    for i in range(len(mins_list)):
        result_list.append(mins_list[i])
    return result_list


# Задача 17
def max_from_interval(list, start_point, end_point):
    result_list = list[start_point:end_point]
    return max(result_list)


# Задача 18
def smaller_than_left(list):
    count = 0
    for i in range (1, len(list)):
        if list[i] < list[i - 1]:
            print("Индекс: " + str(i))
            count += 1
    return count

print(before_min_in_the_end([1, 3, 4, 5, -70, 235, 356457, 432]))