import re
import random
ip=0x1000-1
sp=0x1000-2
class CodeGenerator:
    def __init__(self):
        self.ip=0
        self.lines=[]
        self.labels={}
    def write(self,lines):
        for i in range(len(lines)):
            if ":" in lines[i]:
                split=lines[i].split(":")
                lines[i]=split[1]
                split[0]=split[0].strip()
                split[1]=split[1].strip()
                assert split[0] not in self.labels
                self.labels[split[0]]=self.ip+i
        self.lines+=lines
        self.ip=len(self.lines)
    def print(self,s):
        if len(s)==0:
            return
        inst = [f"MOV 0 {ord(s[0])}","PUTC"]
        prev=ord(s[0])
        for c in s[1:]:
            cur=ord(c)
            if prev<cur:
                inst.append(f"+ 0 {cur-prev}")
            elif cur<prev:
                inst.append(f"- 0 {prev-cur}")
            prev=cur
            inst.append("PUTC")
        self.write(inst)

    def read(self):
        self.write([
            "MOV 1 0",
            "READ",
            "- 0 10",
            f"JZ 0 {self.ip + 8}",
            f"+ 0 10",
            "PUSH_REG 0",
            "+ 1 1",
            f"JMP {self.ip + 1}",
            "MOV_REG 0 1"
        ])
    def gen(self):
        print(self.labels)
        l="\n".join(self.lines)
        for a,b in self.labels.items():
            l=re.sub(f" {a}([ \n])",f" {b}\\1",l)
        return l

sudoku=[23, None, 6, 0, 8, 19, 4, 5, 14, None, None, 24, 21, 16, 17, 9, 13, 15, 12, 22, 11, 7, 10, 2, 18, 11, None, 21, 16, None, 9, 13, 15, 12, 22, 23, 7, None, None, 18, None, None, 6, 0, 8, 19, 4, None, 14, 20, 9, 7, 10, None, 18, None, None, None, 0, 8, 19, None, 5, 14, None, 11, 24, 21, None, None, 23, 13, 15, None, 22, 19, 4, 5, 14, None, 11, 24, 21, 16, None, 9, 13, 15, 12, 22, 23, 7, None, None, 18, None, 1, None, 0, 8, None, 13, 15, 12, 22, 23, 7, 10, None, 18, 11, 1, 6, 0, None, 19, 4, 5, 14, 20, 9, None, 21, 16, None, 8, 23, 1, 6, 0, None, 19, None, None, 14, 17, None, None, 21, 16, 22, 9, 13, 15, 12, 18, 11, 7, 10, 2, 17, 11, 24, 21, 16, 22, 9, 13, 15, 12, 18, 23, 7, 10, 2, 8, None, 1, 6, 0, 20, 19, None, None, 14, 18, None, None, 10, None, None, None, None, 6, None, 20, 19, None, 5, 14, 17, 11, 24, 21, 16, 22, 23, 13, 15, 12, None, 19, 4, None, 14, 17, 11, None, 21, 16, 22, 9, 13, 15, 12, 18, 23, 7, 10, None, 8, None, None, 6, 0, 22, None, 13, 15, 12, 18, 23, None, 10, None, 8, 11, None, 6, None, None, 19, 4, None, 14, 17, 9, 24, 21, 16, 2, None, None, 1, 10, None, None, 19, 4, 5, 0, 17, None, 24, 6, 12, 22, 9, 13, None, 16, 18, 11, 7, 21, 16, 17, 11, 24, 21, 12, 22, 9, 13, 15, 2, 18, 23, None, None, 0, 8, None, None, 6, 14, 20, 19, 4, 5, 12, 18, 9, 7, 15, 0, 8, None, 1, None, 14, 20, None, None, 5, None, None, 11, None, 21, None, 22, 23, 13, None, 14, None, 19, 4, None, 16, 17, 11, None, 21, 12, 22, 9, 13, 15, None, 18, None, None, None, 0, 8, 3, 1, 6, 0, 22, None, 13, 6, None, 18, 23, 7, None, 16, 8, 11, 1, 21, 14, 20, 19, 4, 5, 12, 17, None, None, 15, 6, 2, 8, 23, None, 5, None, None, 19, 4, 21, 0, 17, None, None, 15, None, 22, None, 13, 10, 16, 18, 11, 7, 21, 16, None, 11, None, 15, 12, 22, 9, 13, None, None, 18, None, 7, 6, 0, 8, None, 1, 5, 14, 20, 19, 4, 10, 12, 18, 9, 7, 6, 0, None, None, 1, 5, 14, 20, 19, 4, None, None, 17, 11, None, 15, None, 22, None, 13, 5, 14, None, 19, 4, 21, 16, 17, 11, None, 15, 12, 22, 9, 13, 10, None, 18, None, 7, 6, 0, 8, 3, 1, 15, 0, None, None, 13, 10, 2, 18, 23, 7, 6, 16, 8, 11, None, None, 14, 20, 19, 4, 21, 12, 17, None, None, None, 6, 2, 8, 23, None, 5, 14, 20, 19, 24, 21, 0, 17, None, 13, 15, None, None, 9, 7, 10, 16, 18, 11, None, 21, 16, None, 11, 13, 15, 12, 22, 9, None, None, None, 18, 23, None, 6, None, 8, None, 4, 5, 14, 20, 19, None, 10, 12, 18, 9, None, 6, 0, 8, None, 4, 5, 14, 20, 19, None, 21, None, None, 11, 13, 15, 2, 22, 23, 4, None, 14, None, 19, None, 21, 16, 17, 11, 13, 15, 12, 22, None, 7, 10, None, None, 23, None, 6, 0, 8, None, 13, 15, 0, 22, None, None, 10, 2, 18, 23, None, 6, None, 8, 11, 4, 5, 14, 20, None, None, 21, 12, 17, None]
key_table=[410, 234, 505, 312, 589, 293, 232, 26, 56, 68, 344, 320, 180, 252, 182, 441, 391, 313, 490, 555, 599, 256, 69, 176, 38, 342, 518, 381, 329, 237, 55, 326, 114, 239, 604, 444, 324, 53, 359, 340, 559, 137, 535, 207, 411, 528, 292, 404, 489, 612, 514, 382, 343, 499, 517, 187, 97, 219, 136, 565, 288, 221, 388, 200, 309, 440, 537, 468, 592, 316, 478, 79, 568, 624, 57, 466, 269, 177, 47, 500, 418, 452, 41, 315, 73, 172, 243, 379, 10, 240, 84, 372, 446, 413, 477, 255, 576, 1, 544, 130, 251, 184, 181, 121, 92, 108, 289, 93, 352, 318, 605, 373, 179, 402, 40, 620, 595, 567, 307, 578, 124, 393, 433, 580, 593, 37, 203, 222, 262, 64, 132, 619, 95, 389, 226, 525, 100, 459, 166, 9, 432, 61, 173, 610, 550, 333, 355, 448, 29, 498, 133, 540, 536, 542]
gen=CodeGenerator()
sudoku_addr=0x700
opcode_table_addr=0xb00
stack_base_addr=0x100
check_addr=0x210
flag_addr=12
opcode_table=["VM_OTHER"]*256
opcode_table[ord("+")]="VM_ADD"
opcode_table[ord("-")]="VM_SUB"
opcode_table[ord("*")]="VM_MUL"
opcode_table[ord("%")]="VM_REM"
opcode_table[ord("/")]="VM_DIV"
opcode_table[ord("p")]="VM_POW"
opcode_table[ord("w")]="VM_WRITE"
opcode_table[ord("x")]="VM_READ"
gen.print("flag:")
gen.write([
    f"MOV {opcode_table_addr+i} {opcode_table[i]}" for i in range(len(opcode_table))
])
gen.write([
    f"MOV {sudoku_addr+i} {sudoku[i] if sudoku[i] is not None else random.randint(0,24)}" for i in range(len(sudoku))
])
gen.write([
    # pow(A_reg,B_reg,C_reg)
    f"JMP TEST",
    "POW:MOV 3 1",
    f"POW_CONT:JZ 1 POW_RET",
    "*_REG 3 0",
    "%_REG 3 2",
    "- 1 1",
    f"JMP POW_CONT",
    "POW_RET:MOV_REG 0 3",
    "RET"
])
"""
42 * mul 2 args
43 + add 2 args
45 - sub 2 args
37 % rem 2 args
112 p pow_mod 3 args
119 w write_mem 2 args
120 x read_mem 1 args
101 e exit 0 args
otherwise push
"""
gen.write([
    #REG_A opcode addr
    f"EXEC_VM:MOV_REG 128 0",
        f"_EXEC_VM:- 128 {stack_base_addr}",
            f"JZ 128 _EXEC_VM_RET",
            f"+ 128 {stack_base_addr}",
            "MOV_REG 0 128",
            "- 128 1",
            "READ_MEM 0",
            "CALL INNER_VM",
            "- 10 28",
            "JZ 10 _EXEC_VM_RET",
            "+ 10 28",
        "JMP _EXEC_VM",
    "_EXEC_VM_RET:RET"
])
gen.write([
    #REG_A opcode
    f"INNER_VM:MOV_REG 1 0",
        "MOV_REG 99 0",
        "/ 99 256",
        "JZ 99 EE",
        "JMP VM_OTHER",
        f"EE:+ 0 {opcode_table_addr}",
        f"READ_MEM 0",
        f"MOV_REG {ip} 0"
])
gen.write([
    "VM_ADD:POP 0",
        "POP 1",
        "+_REG 0 1",
        "PUSH_REG 0",
        "RET",
    "VM_SUB:POP 0",
        "POP 1",
        "-_REG 0 1",
        "PUSH_REG 0",
        "RET",
    "VM_MUL:POP 0",
        "POP 1",
        "*_REG 0 1",
        "PUSH_REG 0",
        "RET",
    "VM_DIV:POP 0",
        "POP 1",
        "/_REG 0 1",
        "PUSH_REG 0",
        "RET",
    "VM_REM:POP 0",
        "POP 1",
        "%_REG 0 1",
        "PUSH_REG 0",
        "RET",
    "VM_POW:POP 0",
	    "POP 1",
	    "POP 2",
	    f"CALL POW",
        "PUSH_REG 0",
	    "RET",
    "VM_WRITE:POP 0",
        "POP 1",
        "WRITE_MEM 0 1",
        "RET",
    "VM_READ:POP 0",
        "READ_MEM 0",
        f"PUSH_REG 0",
        "RET",
    "VM_EXIT:MOV 10 28",
        "RET",
    f"VM_OTHER:- 1 128",
        "PUSH_REG 1",
        "RET",
])
gen.write([
    f"TEST:MOV {sp} 12",
])
gen.read()
gen.write([
    "- 0 77",
    "JZ 0 CHECK",
    "INCORRECT:MOV 0 0"
])
gen.print("Incorrect")
gen.write([
    "RET"
])
gen.write([
    f"CHECK:MOV {sp} {stack_base_addr}",
    "PUSH 101"
])
for i in range(77):
    gen.write([
        "PUSH 119",
        "PUSH 43",
        f"PUSH {key_table[2 * i] + 128}",
        f"PUSH {sudoku_addr + 128}",
        "PUSH 37",
        "PUSH 120",
        f"PUSH {flag_addr + i + 128}",
        f"PUSH {23 + 128}",
        "PUSH 119",
        "PUSH 43",
        f"PUSH {key_table[2 * i + 1] + 128}",
        f"PUSH {sudoku_addr + 128}",
        "PUSH 37",
        "PUSH 120",
        f"PUSH {flag_addr + i + 128}",
        f"PUSH {25 + 128}",
    ])
gen.write([
    f"MOV_REG 0 {sp}",
    f"MOV {sp} {0xc00}",
    "CALL EXEC_VM",
])
gen.write([
    "MOV 99 0",
    "CHECK_LINE:MOV 66 0",
        f"MOV 33 {check_addr}",
        "MOV 77 0",
        "MOV 88 1",
        "CHECK_LINE_LOOP:WRITE_MEM 33 77",
            "+ 33 1",
            f"- 33 {check_addr+25}",
            "JZ 33 CHECK_LINE_LOOP_EXIT",
            f"+ 33 {check_addr+25}",
            "JMP CHECK_LINE_LOOP",
        f"CHECK_LINE_LOOP_EXIT:MOV 22 {sudoku_addr}",
        "+_REG 22 99",
        "MOV 55 0",
        "CHECK_LINE_FINAL_LOOP:MOV_REG 11 22",
            "READ_MEM 11",
            f"+ 11 {check_addr}",
            "WRITE_MEM 11 88",
            "+ 22 25",
            "+ 55 1",
            "- 55 25",
            "JZ 55 CHECK_LINE_FINAL_LOOP_EXIT",
            "+ 55 25",
            "JMP CHECK_LINE_FINAL_LOOP",
        f"CHECK_LINE_FINAL_LOOP_EXIT:MOV 22 {check_addr}",
        "CHECK_LINE_FINAL_FINAL_LOOP:MOV_REG 11 22",
            "READ_MEM 11",
            "JZ 11 INCORRECT",
            "+ 22 1",
            f"- 22 {check_addr+25}",
            "JZ 22 CHECK_LINE_FINISH",
            f"+ 22 {check_addr+25}",
            "JMP CHECK_LINE_FINAL_FINAL_LOOP",
        "CHECK_LINE_FINISH:+ 99 1",
        "- 99 25",
        "JZ 99 CHECK_ROW_NEXT",
        "+ 99 25",
        "JMP CHECK_LINE"
])
gen.write([
    "CHECK_ROW_NEXT:MOV 99 0",
    "CHECK_ROW:MOV 66 0",
        f"MOV 33 {check_addr}",
        "MOV 77 0",
        "MOV 88 1",
        "CHECK_ROW_LOOP:WRITE_MEM 33 77",
            "+ 33 1",
            f"- 33 {check_addr+25}",
            "JZ 33 CHECK_ROW_LOOP_EXIT",
            f"+ 33 {check_addr+25}",
            "JMP CHECK_ROW_LOOP",
        f"CHECK_ROW_LOOP_EXIT:MOV 22 {sudoku_addr}",
        "MOV_REG 11 99",
        "* 11 25",
        "+_REG 22 11",
        "MOV 55 0",
        "CHECK_ROW_FINAL_LOOP:MOV_REG 11 22",
            "READ_MEM 11",
            f"+ 11 {check_addr}",
            "WRITE_MEM 11 88",
            "+ 22 1",
            "+ 55 1",
            "- 55 25",
            "JZ 55 CHECK_ROW_FINAL_LOOP_EXIT",
            "+ 55 25",
            "JMP CHECK_ROW_FINAL_LOOP",
        f"CHECK_ROW_FINAL_LOOP_EXIT:MOV 22 {check_addr}",
        "CHECK_ROW_FINAL_FINAL_LOOP:MOV_REG 11 22",
            "READ_MEM 11",
            "JZ 11 INCORRECT",
            "+ 22 1",
            f"- 22 {check_addr+25}",
            "JZ 22 CHECK_ROW_FINISH",
            f"+ 22 {check_addr+25}",
            "JMP CHECK_ROW_FINAL_FINAL_LOOP",
        "CHECK_ROW_FINISH:+ 99 1",
        "- 99 25",
        "JZ 99 CHECK_BOX_NEXT",
        "+ 99 25",
        "JMP CHECK_ROW"
])
gen.write([
    "CHECK_BOX_NEXT:MOV 11 0",
    "CHECK_BOX_1:MOV 22 0",
        "CHECK_BOX_2:MOV 0 0",
            f"MOV 33 {check_addr}",
            "MOV 34 0",
            "CHECK_BOX_CLEAR_LOOP:WRITE_MEM 33 34",
                "+ 33 1",
                f"- 33 {check_addr+25}",
                "JZ 33 CHECK_BOX_CLEAR_LOOP_EXIT",
                f"+ 33 {check_addr+25}",
                "JMP CHECK_BOX_CLEAR_LOOP",
            #15 counter, 16 ptr
            "CHECK_BOX_CLEAR_LOOP_EXIT:MOV 15 0",
            f"MOV 16 {sudoku_addr}",
            f"MOV_REG 17 11",
            f"* 17 5",
            "+_REG 16 17",
            "MOV_REG 17 22",
            "* 17 125",
            "+_REG 16 17",
            "MOV 87 1",
            "CHECK_BOX_WRITE_LOOP:MOV_REG 17 16",
                "READ_MEM 17",
                f"+ 17 {check_addr}",
                "WRITE_MEM 17 87",
                "+ 16 1",
                "+ 15 1",
                "- 15 25",
                "JZ 15 CHECK_BOX_WRITE_LOOP_EXIT",
                "+ 15 25",
                "MOV_REG 19 15",
                "% 19 5",
                "JZ 19 ADD_20",
                "JMP CHECK_BOX_WRITE_LOOP",
                "ADD_20:+ 16 20",
                "JMP CHECK_BOX_WRITE_LOOP",
            f"CHECK_BOX_WRITE_LOOP_EXIT:MOV 33 {check_addr}",
            "CHECK_BOX_FINAL:MOV_REG 34 33",
                "READ_MEM 34",
                "JZ 34 INCORRECT",
                "+ 33 1",
                f"- 33 {check_addr+25}",
                "JZ 33 CHECK_BOX_FINAL_EXIT",
                f"+ 33 {check_addr+25}",
                "JMP CHECK_BOX_FINAL",
            "CHECK_BOX_FINAL_EXIT:+ 22 1",
            "- 22 5",
            "JZ 22 CHECK_BOX_2_EXIT",
            "+ 22 5",
            "JMP CHECK_BOX_2",
        "CHECK_BOX_2_EXIT:+ 11 1",
        "- 11 5",
        "JZ 11 CHECK_BOX_1_EXIT",
        "+ 11 5",
        "JMP CHECK_BOX_1",
    "CHECK_BOX_1_EXIT:MOV 0 0"
])
gen.print("Correct! In case you find a fake flag, I'll leave SHA256 hash of the true flag here:8d5f1becd60f19181c89d6563677b941cc7ceec6298d80ffea7d17f537fb5c11")
open("code.txt","w").write(gen.gen())