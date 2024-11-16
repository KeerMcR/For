numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number > 1:  # Исключаем единицу из перебора
        is_prime = True
        for i in range(2, int(number / 2) + 1):  # Проверяем делители до половины числа, поскольку дальше нет смысла
            if number % i == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)

print(primes)
print(not_primes)
