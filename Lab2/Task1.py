print("Номер варианта: " + str(((13 - 1) % 10) + 1))

def same_in_two_lists(list1, list2):
    return sorted(list(set(list1) & set(list2)))

