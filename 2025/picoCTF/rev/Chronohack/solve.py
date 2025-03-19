import random
import time
from pwn import remote,context

def get_random(length,k):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int(k))  # seeding with current time 
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

sock=remote(SERVER,PORT)
k=time.time()*1000
context.log_level="debug"
sock.recvuntil(b"!")
token_length = 20
for i in range(50):
    sock.sendline(get_random(token_length,k-i-50*8))
    sock.recvuntil(b"!")