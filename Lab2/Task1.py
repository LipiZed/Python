print("Номер варианта первой задачи: " + str(((13 - 1) % 10) + 1))

def same_in_two_lists(list1, list2):
    return sorted(list(set(list1) & set(list2)))

print(same_in_two_lists([1, 2, 3], [2, 3, 4]))
print("Номер варианта второй задачи: " + str(((13 - 1) % 13) + 1))


def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result

def LCA():
    p_tree = dict()
    n = int(input())
    for i in range(n - 1):
        child, parent = input().split()
        p_tree[child] = parent

    m = int(input())
    for i in range(m):
        child_1, child_2 = input().split()
        ancestors_for_1 = set(ancestors(child_1, p_tree))
        for ancestor in ancestors(child_2, p_tree):
            if ancestor in ancestors_for_1:
                print(ancestor)
                break

