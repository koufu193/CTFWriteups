from Crypto.Util.number import bytes_to_long
sudoku=[23, None, 6, 0, 8, 19, 4, 5, 14, None, None, 24, 21, 16, 17, 9, 13, 15, 12, 22, 11, 7, 10, 2, 18, 11, None, 21, 16, None, 9, 13, 15, 12, 22, 23, 7, None, None, 18, None, None, 6, 0, 8, 19, 4, None, 14, 20, 9, 7, 10, None, 18, None, None, None, 0, 8, 19, None, 5, 14, None, 11, 24, 21, None, None, 23, 13, 15, None, 22, 19, 4, 5, 14, None, 11, 24, 21, 16, None, 9, 13, 15, 12, 22, 23, 7, None, None, 18, None, 1, None, 0, 8, None, 13, 15, 12, 22, 23, 7, 10, None, 18, 11, 1, 6, 0, None, 19, 4, 5, 14, 20, 9, None, 21, 16, None, 8, 23, 1, 6, 0, None, 19, None, None, 14, 17, None, None, 21, 16, 22, 9, 13, 15, 12, 18, 11, 7, 10, 2, 17, 11, 24, 21, 16, 22, 9, 13, 15, 12, 18, 23, 7, 10, 2, 8, None, 1, 6, 0, 20, 19, None, None, 14, 18, None, None, 10, None, None, None, None, 6, None, 20, 19, None, 5, 14, 17, 11, 24, 21, 16, 22, 23, 13, 15, 12, None, 19, 4, None, 14, 17, 11, None, 21, 16, 22, 9, 13, 15, 12, 18, 23, 7, 10, None, 8, None, None, 6, 0, 22, None, 13, 15, 12, 18, 23, None, 10, None, 8, 11, None, 6, None, None, 19, 4, None, 14, 17, 9, 24, 21, 16, 2, None, None, 1, 10, None, None, 19, 4, 5, 0, 17, None, 24, 6, 12, 22, 9, 13, None, 16, 18, 11, 7, 21, 16, 17, 11, 24, 21, 12, 22, 9, 13, 15, 2, 18, 23, None, None, 0, 8, None, None, 6, 14, 20, 19, 4, 5, 12, 18, 9, 7, 15, 0, 8, None, 1, None, 14, 20, None, None, 5, None, None, 11, None, 21, None, 22, 23, 13, None, 14, None, 19, 4, None, 16, 17, 11, None, 21, 12, 22, 9, 13, 15, None, 18, None, None, None, 0, 8, 3, 1, 6, 0, 22, None, 13, 6, None, 18, 23, 7, None, 16, 8, 11, 1, 21, 14, 20, 19, 4, 5, 12, 17, None, None, 15, 6, 2, 8, 23, None, 5, None, None, 19, 4, 21, 0, 17, None, None, 15, None, 22, None, 13, 10, 16, 18, 11, 7, 21, 16, None, 11, None, 15, 12, 22, 9, 13, None, None, 18, None, 7, 6, 0, 8, None, 1, 5, 14, 20, 19, 4, 10, 12, 18, 9, 7, 6, 0, None, None, 1, 5, 14, 20, 19, 4, None, None, 17, 11, None, 15, None, 22, None, 13, 5, 14, None, 19, 4, 21, 16, 17, 11, None, 15, 12, 22, 9, 13, 10, None, 18, None, 7, 6, 0, 8, 3, 1, 15, 0, None, None, 13, 10, 2, 18, 23, 7, 6, 16, 8, 11, None, None, 14, 20, 19, 4, 21, 12, 17, None, None, None, 6, 2, 8, 23, None, 5, 14, 20, 19, 24, 21, 0, 17, None, 13, 15, None, None, 9, 7, 10, 16, 18, 11, None, 21, 16, None, 11, 13, 15, 12, 22, 9, None, None, None, 18, 23, None, 6, None, 8, None, 4, 5, 14, 20, 19, None, 10, 12, 18, 9, None, 6, 0, 8, None, 4, 5, 14, 20, 19, None, 21, None, None, 11, 13, 15, 2, 22, 23, 4, None, 14, None, 19, None, 21, 16, 17, 11, 13, 15, 12, 22, None, 7, 10, None, None, 23, None, 6, 0, 8, None, 13, 15, 0, 22, None, None, 10, 2, 18, 23, None, 6, None, 8, 11, 4, 5, 14, 20, None, None, 21, 12, 17, None]
key_table=[410, 234, 505, 312, 589, 293, 232, 26, 56, 68, 344, 320, 180, 252, 182, 441, 391, 313, 490, 555, 599, 256, 69, 176, 38, 342, 518, 381, 329, 237, 55, 326, 114, 239, 604, 444, 324, 53, 359, 340, 559, 137, 535, 207, 411, 528, 292, 404, 489, 612, 514, 382, 343, 499, 517, 187, 97, 219, 136, 565, 288, 221, 388, 200, 309, 440, 537, 468, 592, 316, 478, 79, 568, 624, 57, 466, 269, 177, 47, 500, 418, 452, 41, 315, 73, 172, 243, 379, 10, 240, 84, 372, 446, 413, 477, 255, 576, 1, 544, 130, 251, 184, 181, 121, 92, 108, 289, 93, 352, 318, 605, 373, 179, 402, 40, 620, 595, 567, 307, 578, 124, 393, 433, 580, 593, 37, 203, 222, 262, 64, 132, 619, 95, 389, 226, 525, 100, 459, 166, 9, 432, 61, 173, 610, 550, 333, 355, 448, 29, 498, 133, 540, 536, 542]
def split_bytes(c):
    result=[]
    for t in c:
        result+=[t%23,t%25]
    return result

def check_line(line):
    return len(set(line))==25

def get_box(su,x,y):
    c=[]
    for i in range(5*y,5*y+5):
        for j in range(5*x,5*x+5):
            c.append(su[j+25*i])
    return c

def check_sat(su):
    for i in range(25):
        if not check_line(su[i*25:i*25+25]):
            return False
        if not check_line(su[i::25]):
            return False
        if not check_line(get_box(su,i%5,i//5)):
            return False
    return True

def check(c:bytes)->bool:
    f=split_bytes(c)
    if len(f)!=len(key_table):
        return False
    sudoku_cpy=sudoku[:]
    for a,b in zip(key_table,f):
        sudoku_cpy[a]=b
    return check_sat(sudoku_cpy)

flag=input("flag:")
print(["Incorrect","Correct"][check(flag.encode())])