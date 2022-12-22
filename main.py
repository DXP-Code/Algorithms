# возведение в степень по модулю (a^x mod m);
# вычисление наибольшего общего делителя (НОД (a, b));
# вычисление мультипликативной инверсии (x^(-1) mod m);
# проверки чисел на простоту (тест Ферма, тест Миллера-Рабина);
# генерации больших простых чисел.
import math
import random
def miller_rabin(n, k):
    if n == 2:
        return "Число простое"

    if n % 2 == 0:
        return "Число не простое"

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for x in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for x in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return "Число не простое"
    return "Число простое"
def rand_prime():
    while True:
        p = random.randrange(1000001, 10000000,
                             2)  # randrange - возвращает случайное целое число в заданном диапазоне, т.е. начало и конец.
        if all(p % n != 0 for n in range(3, int((pow(p, 0.5)) + 1), 2)):
            return p


def CheckIfProbablyPrime(x):
    truthfulness = pow(2, x - 1, x) == 1
    if truthfulness == True:
        return "Число простое"
    else:
        return "Число не простое"

# main
while True:
    choice = int(input("\n1.Найти степень числа по модулю\n2.Найти НОД\n3.Мультипликативной инверсии (x^(-1) по модулю."
                       "\n4.Генерации больших простых чисел\n6.Выход из программы\n"))
    if choice == 1:
        a = int(input())
        x = int(input())
        m = int(input())
        print(pow(a, x, m))
    elif choice == 2:
        a = int(input())
        x = int(input())
        print(math.gcd(a, x))
    elif choice == 3:
        x = int(input())
        m = int(input())
        multiplicative_inversion = x % m
        print(pow(multiplicative_inversion, -1))
    elif choice == 4:
        print(rand_prime())
        choicePrim = int(
            input("Дополнительный алгоритм для проверки числа на простоту:\n1.Вручную\n2.Использовать текущее число\n"))
        if choicePrim == 1:
            x = int(input("Введите число: "))
            print("тест Ферма: ", CheckIfProbablyPrime(x))
            print("Тест Миллера-Рабина: ", miller_rabin(x, 100))
        else:
            x = rand_prime()
            print("тест Ферма: ", CheckIfProbablyPrime(x))
            print("Тест Миллера-Рабина: ", miller_rabin(x, 100))
    elif choice == 6:
        break
