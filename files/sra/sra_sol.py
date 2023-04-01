from re import I
from Crypto.Util.number import getPrime, inverse, bytes_to_long, isPrime
from string import ascii_letters, digits
from random import choice


from pwn import remote
import sys
from string import ascii_letters, digits
from Crypto.Util.number import long_to_bytes
from itertools import combinations


con = remote("saturn.picoctf.net", sys.argv[0])
e = 65537
con.recvuntil(b'anger = ')
c = int(con.readline().decode())
con.recvuntil(b'envy = ')
d = int(con.readline().decode())
print('factoring...')
fac = [a for a, b in list(factor(d*e-1)) for _ in range(b)]
for r in range(2, len(fac)):
    for i in combinations(fac, r):
        p = product(i) + 1
        if p.nbits() != 128 or not is_prime(p):
            continue
        m = long_to_bytes(int(pow(c, d, int(p))))
        if len(m) != 16:
            continue
        con.recvuntil(b'> ')
        con.sendline(m)
        con.interactive()

# pride = "".join(choice(ascii_letters + digits) for _ in range(16))

# gluttony = getPrime(128) #p
# greed = getPrime(128)   #q
# lust = gluttony * greed # n
# sloth = 65537 # e
# phi = (gluttony - 1) * (greed - 1)
# envy = inverse(sloth, phi)

# )
# print(envy * sloth % phi)

# anger = pow(bytes_to_long(pride.encode()), sloth, lust)

# print(lust)
# print(f"{anger = }")
# print(f"{envy = }")


# print("vainglory?")
# vainglory = input("> ").strip()

# if vainglory == pride:
#     print("Conquered!")
#     with open("/challenge/flag.txt") as f:
#         print(f.read())
# else:
#     print("Hubris!")
