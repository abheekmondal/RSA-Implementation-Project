import sys

def encrypt(n, e, m):
    return pow(m, e, n)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python encrypt.py [n] [e] [plaintext]")
        sys.exit(1)

    n = int(sys.argv[1])
    e = int(sys.argv[2])
    m = int(sys.argv[3])

    ciphertext = encrypt(n, e, m)
    print(ciphertext)
