import math


print("Вариант первого задания:", (((13-1)%12) + 1))

print("Функция 1. Найти сумму простых делителей числа.")
def sum_of_prime_div(n):
    if n <= 1:
        return 0
    primes = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            primes.append(i)
            while n % i == 0:
                n //= i
    total = 1
    for p in primes:
        if p == 2:
            continue
        total *= p
    return total

print("Функция 2. Найти количество нечетных цифр числа, больших 3.")
def count_odd(n):
    str_n = str(n)
    count = 0
    for i in range(len(str_n)):
        digit = int(str_n[i])
        if digit % 2 != 0 and digit > 3:
            count += 1
    return count

print("Функция 3. Найти произведение таких делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа.")
def sum_of_div(n):
    str_n = str(n)
    sum_n = sum(int(i) for i in str_n)
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            dig_sum = sum(int(j) for j in str(i))
            if dig_sum < sum_n:
                divs.append(i)
    if not divs:
        return 0
    return int(math.prod(divs))

