import random
flag=[145, 233, 148, 144, 2, 16, 109, 230, 148, 219, 171, 255, 113, 14, 128, 224, 141, 88, 73, 85, 215, 93, 55, 104, 126, 135, 209, 154, 99, 229, 155, 250, 172, 252, 102, 29, 73, 25, 248, 47, 184, 126, 153, 187, 31, 72, 21, 236, 141]
for s in range(0,256*49):
    random.seed(s)
    dec_flag=b"".join([(a^random.randint(0,255)).to_bytes() for a in flag])
    if dec_flag.startswith(b"fwectf"):
        print(dec_flag.decode())
