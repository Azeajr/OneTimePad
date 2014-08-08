'''
Created on Aug 5, 2014

@author: root
'''
import sys

MSGS = []
I = open('Input.txt', 'r')
K = open('Key.txt', 'w')
O = open('Output.txt','w')
for line in I:
    MSGS.append(line.rstrip('\n'))



#MSGS = ["this", "that"]

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    this=open("/dev/urandom").read(size)
    K.write(this.encode('hex') + "\n")
    return this

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    O.write(c.encode('hex') + "\n")
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
        
        
if __name__ == "__main__":
    main()
