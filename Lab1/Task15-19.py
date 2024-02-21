def count_after_max(list):
    a = max(list)
    index = list.index(a)
    count = 0
    for i in range (index + 1, len(list)):
        count += 1
    return count


