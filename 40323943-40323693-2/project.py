import random
import math

def is_prime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bit_length=8):
    while True:
        num = random.getrandbits(bit_length)
        num |= (1 << bit_length - 1) | 1
        if is_prime(num):
            return num

p = generate_prime(8)
q = generate_prime(8)
while p == q:
    q = generate_prime(8)
print("Primes:", p, q)