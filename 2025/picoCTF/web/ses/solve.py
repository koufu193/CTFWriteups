import time

from utils import *
from mersenne import *
def handle_data(data):
    data=data.split("\"")[1]
    return int(data.replace("=",""))
def get_state(token):
    i = send_email("user@ses", "", "", token)
    data = get_email(i, token)["data"]
    #print(data)
    s0,s1=recover(handle_data(data))
    s0 = untemper(s0)
    s1 = untemper(s1)
    return s0,s1
def guess_state(token):
    ss=[0]*624
    for i in range(0,624,2):
        print(i)
        aa,bb=get_state(token)
        ss[i]=aa
        ss[i+1]=bb
        time.sleep(0.5)
    return ss
