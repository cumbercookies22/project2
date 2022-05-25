# coding: utf-8
from pwn import *
def chall09():
    p=process("./chall_09")
    elf=ELF("./chall_09")
    payload=((xor(elf.string(elf.sym.key),b'\x69'))+b'\x00\n')
    p.send(payload)
    p.interactive()
    
chall09()
