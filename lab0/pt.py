from pwn import * 

#r = remote('127.0.0.1', '8888')
r = process('./pwntools')
r.recvuntil('number :)\n')

p = p32(0xdeadbeef)

r.send(p)

r.recvline()
for i in range(1000):
    q = r.recvuntil(' = ?').replace(' = ?', '')
    print q
    ans = eval(q)
    r.sendline(str(ans))

r.interactive()


