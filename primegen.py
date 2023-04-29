import sys
import random

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if miller_rabin(candidate, 5):
            return candidate

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python primegen.py [bits]")
        sys.exit(1)

    bits = int(sys.argv[1])
    prime = generate_prime(bits)
    print(prime)
