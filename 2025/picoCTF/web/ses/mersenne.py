#https://inaz2.hatenablog.com/entry/2016/03/07/194147 や Phindなどから
def guess(s0, s1, s397):
    # y の計算
    y = (s0 & 0x80000000) | (s1 & 0x7fffffff)
    # 右シフトとXOR
    next_state = s397 ^ (y >> 1)
    # 最下位ビットが1ならば XOR する
    if y & 1:
        next_state ^= 0x9908B0DF
    return next_state

import random
def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y

def temper(y):
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)
    return y

def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y
import random
def recover(value):
    return value&((1<<32)-1),((value>>32)<<1)|(random.choice([0,1]))