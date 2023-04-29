import sys

def decrypt(n, d, c):
    return pow(c, d, n)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py [n] [d] [ciphertext]")
        sys.exit(1)

    n = int(sys.argv[1])
    d = int(sys.argv[2])
    c = int(sys.argv[3])

    plaintext = decrypt(n, d, c)
    print(plaintext)
