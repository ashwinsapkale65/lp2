import random
import math

# Generate a random prime number
def generate_prime():
    while True:
        prime = random.randint(100, 1000)
        if all(prime % i != 0 for i in range(2, int(math.sqrt(prime))+1)):
            return prime

# Compute the modular inverse of a number
def modinv(a, m):
    return next(i for i in range(1, m) if (a * i) % m == 1)

# Generate public and private keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p-1) * (q-1)
    e = random.randint(1, phi_n)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)
    d = modinv(e, phi_n)
    return ((n, e), (n, d))

# Encrypt a message using the public key
def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

# Decrypt a message using the private key
def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)

# Test the RSA implementation
public_key, private_key = generate_keys()
print("Public key:", public_key)
print("Private key:", private_key)

message = 2737 
print("Original message:", message)

ciphertext = encrypt(message, public_key)
print("Encrypted message:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
