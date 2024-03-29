logo = '''

    ######## ##        ######      ###    ##     ##    ###    ##       
    ##       ##       ##    ##    ## ##   ###   ###   ## ##   ##       
    ##       ##       ##         ##   ##  #### ####  ##   ##  ##       
    ######   ##       ##   #### ##     ## ## ### ## ##     ## ##       
    ##       ##       ##    ##  ######### ##     ## ######### ##       
    ##       ##       ##    ##  ##     ## ##     ## ##     ## ##       
    ######## ########  ######   ##     ## ##     ## ##     ## ######## 

           ######  #### ########  ##     ## ######## ########          
          ##    ##  ##  ##     ## ##     ## ##       ##     ##         
          ##        ##  ##     ## ##     ## ##       ##     ##         
          ##        ##  ########  ######### ######   ########          
          ##        ##  ##        ##     ## ##       ##   ##           
          ##    ##  ##  ##        ##     ## ##       ##    ##          
           ######  #### ##        ##     ## ######## ##     ##         

'''

print(logo)

import random
from primePy import primes
import time

F = primes.first(1000)

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def primitiveroot(q):    
    qi = F.index(q)
    for i in range(0, qi+1):
        if gcd(F[i], q) == 1:
            return F[i]


def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def generate_keypair(p, g, x):
    y = mod_exp(g, x, p)
    return (y, p, g), (x, p, g)

def elgamal_encrypt(plain_text, public_key):
    y, p, g = public_key
    k = random.randint(1, p - 1)
    c1 = mod_exp(g, k, p)
    s = mod_exp(y, k, p)
    c2 = [(s * ord(char)) % p for char in plain_text]
    return c1, c2

def elgamal_decrypt(c1, c2, private_key):
    x, p, g = private_key
    s_inv = mod_exp(c1, p - 1 - x, p)
    decrypted_message = ''.join([chr((c * s_inv) % p) for c in c2])
    return decrypted_message


p = random.choice(F)
g = primitiveroot(p)
x = random.randint(1, p - 1)  
public_key, private_key = generate_keypair(p, g, x)

# Encryption
message = input("Enter the message to encrypt >> ")
c1, c2 = elgamal_encrypt(message, public_key)
print(f"Encrypted message: {c1}, {c2}")

time.sleep(10)

# Decryption
decrypted_message = elgamal_decrypt(c1, c2, private_key)
print(f"Decrypted message: {decrypted_message}")
