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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    old_r, r = phi, e
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_t % phi

n = p * q
phi_n = (p - 1) * (q - 1)
e = 3
while gcd(e, phi_n) != 1:
    e += 2
d = mod_inverse(e, phi_n)

print("n:", n)
print("phi(n):", phi_n)
print("e:", e)
print("d:", d)

def encrypt(msg, e, n):
    return pow(msg, e, n)

def decrypt(cipher, d, n):
    return pow(cipher, d, n)

message = 123
cipher = encrypt(message, e, n)
decrypted = decrypt(cipher, d, n)

print("Original number:", message)
print("Encrypted:", cipher)
print("Decrypted:", decrypted)

def encrypt(msg, e, n):
    return pow(msg, e, n)

def decrypt(cipher, d, n):
    return pow(cipher, d, n)

message = 123
cipher = encrypt(message, e, n)
decrypted = decrypt(cipher, d, n)

print("Original number:", message)
print("Encrypted:", cipher)
print("Decrypted:", decrypted)