import sys

def keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    return ((n, e), (n, d))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('No modular inverse exists')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python keygen.py [prime1] [prime2]")
        sys.exit(1)

    prime1 = int(sys.argv[1])
    prime2 = int(sys.argv[2])

    public_key, private_key = keygen(prime1, prime2)

    print("Public Key:", public_key)
    print("Private Key:", private_key)
