import random
from math import gcd

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def generate_key_pair():
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(c), e, n) for c in message]

def decrypt(cipher_text, private_key):
    d, n = private_key
    return ''.join([chr(pow(c, d, n)) for c in cipher_text])

def main():
    public_key, private_key = generate_key_pair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter the message to be encrypted: ")
    encrypted_message = encrypt(message, public_key)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)

if __name__ == '__main__':
    main()
