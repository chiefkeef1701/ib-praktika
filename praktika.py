import random




def find_modular_inverse(e, f):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = extended_gcd(e, f)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {e} mod {f}, since gcd({e}, {f}) = {gcd} != 1")
    return x % f






def find_special_prime(f):
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    candidates = [num for num in range(2, f) if is_prime(num) and gcd(num, f) == 1]

    if not candidates:
        return None 

    return random.choice(candidates)


print("Введите 1 для алгоритма шифрования RSA. Для протокола Диффи-Хелмана введите 2")
choice = int(input())
if choice == 1:
    print("Введите два различных простых числа p и q")
    p = int(input("p="))
    q = int(input("q="))
    n = p * q
    print("Модуль n равен",n)
    f = (p-1)*(q-1)
    print("Результат вычисления функции Эйлера f равен",f)
    e = find_special_prime(f)
    print("Случайно подобранное взаимно простое с f число e равно",e)
    print("{",e,"},{",n,"} - открытый ключ")
    d = find_modular_inverse(e,f)
    print("Число, обратное e по модулю f равно:",d)
    print("{",d,"},{",n,"} - закрытый ключ")
    P = int(input("Введите ваше сообщение P:"))
    E = (P**e)%n
    print("Ваш собеседник получил сообщение E=",E)
    A = (E**d)%n
    print("Раскодированное с помощью закрытого ключа сообщение:",A)
if choice == 2:
    print("Введите два числа g и p, степени a и b")
    g = int(input("g="))
    p = int(input("p="))
    a = int(input("a="))
    b = int(input("b="))
    A = (g**a)%p
    B = (g**b)%p
    KA = (B**a)%p
    KB = (A**b)%p
    if KA == KB:
        print(KA)
