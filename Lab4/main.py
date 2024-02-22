from sympy import symbols, solve, simplify
def task1(path_to_file):
    f = open(path_to_file)
    first = f.readline().split(" ")
    n = int(first.pop(0))
    k = int(first.pop(0))
    a = [int(x) for x in f]
    st = 10**10
    fin = 10**10
    summa = 10**10
    for i in range(2*k,n):
        st = min(st, a[i-2*k])
        fin = min(fin, st + a[i-k])
        summa = min(summa, fin + a[i])
    print(summa)


def task2(path_to_file, start_point, end_point):
    f = open(path_to_file)
    str = f.readline()
    max_step = 0
    cof_list = []
    for i in range(0, len(str)):
        if str[i] == 'x' and i != 0:
            j = 1
            cof = ''
            while str[i - j].isdigit() and (i-j) >= 0:
                cof += str[i-j]
                j += 1
            cof_list.append(cof[::-1])
        if str[i] == '^':
            if int(str[i + 1]) > max_step:
                max_step = int(str[i + 1])

    print(max_step)
    print(cof_list)
    x_range = []
    for i in range(start_point, end_point + 1):
        x_range.append(i)
    str = str.replace('^', '**')
    terms = str.split('x')
    str = ' * x'.join(terms)
    x = symbols('x')
    equation = eval(str)
    solutions = solve(equation, x)
    print(solutions)
    return 0


task2('files/task2', 1, 5)


