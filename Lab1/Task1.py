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

