#!/usr/bin/env python3
from curses.ascii import isalpha
from Crypto.Util.number import *
import time
from pwn import *
from re import *
import sys
from more_itertools import value_chain

# with open("key.txt", "r") as f:
#     SECRET_KEY = f.read()

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

# print(len(Sbox))
# # Leaks one bit of information every operation
leak_buf = []
def leaky_aes_secret(data_byte, key_byte):
    index = data_byte ^ ord(key_byte)
    out = Sbox[index]
    leak_buf.append(out & 0x01)
    return out


# # Simplified version of AES with only a single encryption stage
def encrypt(plaintext, key):
    global leak_buf
    leak_buf = []
    ciphertext = [leaky_aes_secret(plaintext[i], key[i]) for i in range(16)]
    return ciphertext

# Leak the number of 1 bits in the lowest bit of every SBox output
def encrypt_and_leak(plaintext, key):
    ciphertext = encrypt(plaintext, key)
    ciphertext = None # throw away result
    return leak_buf.count(1)

def encrypt_and_lea(plaintext):
    ciphertext = encrypt(plaintext, SECRET_KEY)
    ciphertext = None # throw away result
    time.sleep(0.01)
    return leak_buf.count(1)

# pt = hex(bytes_to_long(f"{chr(98)*16}".encode()))[2:]
# pt = '00000000000000000000000000000000'

# if len(pt) != 32:
#     print("Invalid length")
#     sys.exit(0)

mapping = {i:[] for i in [hex(v)[2:] for v in range(0, 0xff +0x1)]}

for j in range(0, 0xff + 0x1):
    for i in range(65, 91):
        pt = hex(bytes_to_long(f"{chr(i)*16}".encode()))[2:]
        pt = bytes.fromhex(pt)
        encrypt_and_leak(pt, f'{chr(j)*16}')
        # print("leakage result:", encrypt_and_leak(pt), chr(i))
        mapping[hex(j)[2:]].append(leak_buf[0])
#         # print(leak_buf)


def encryp(pt):
    conn = remote('saturn.picoctf.net', int(sys.argv[1]))
    conn.sendlineafter("hex: ", pt)
    val = int(findall('\d+',conn.recv().decode())[0])
    conn.close()
    return val


leak_buf = []
out = []
full = []

flag = ''

for k in range(0, 16):
    out = []
    first,start = True, False
    checkk = False
    teach = True
    third = False
    prev = 0
    h = 0
    j = 0
    try:
        for i in range(0, 256+1):
            pt = hex(bytes_to_long(f"{chr(i)}".encode()))[2:]
            pt = pt + "00"*(15 - k)
            pt = pt.zfill(32)
            val = encryp(pt)
            if val > h:
                h = val
            if first:
                prev = val
            elif (start and teach):
                if val == prev:
                    c = hex(bytes_to_long('c'.encode()))[2:]
                    c = c + '00'*13
                    c = c.zfill(32)
                    check = encryp(c)
                    out.extend([1, 1]) if check <= val  else out.extend([0,0])
                elif val > prev:
                    out.extend([0, 1])
                elif prev > val:
                    out.extend([1, 0])
                start = False
                teach = False
            else:
                if val > prev:
                    out.append(1)
                elif val == prev and (val == h):
                    out.append(1)
                else:
                    out.append(0)
            first = False
            start = True
            j += 1
            prev = val
        ind = list(mapping.values()).index(out)
        f = str(list(mapping.keys())[ind]).zfill(2)
        flag = flag + f
        print("Added: ", f)
        print("+++++++++++++++++Flag:",flag)
        full.append(out)

    except:
        print("failed bit: ")
        print(out)
        full.append(out)
        if out[0] == 0:
            out[0], out[1] = 1,1
        else:
            out[0], out[1] = 0,0
        try:
            ind = list(mapping.values()).index(out)
            flag = flag + list(mapping.keys())[ind]
        except:
            flag = flag +'-'
            continue

print(flag)
assert len(flag) == 32, "not done"
print("Flag bruteforced!!!!!!!!!!!!!!!!!!!!!!!!")


