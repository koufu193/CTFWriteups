code=open("code.txt").read().splitlines()
opcode_table=[
    "READ","PUTC","MOV","PUSH","PUSH_REG","POP","MOV_REG","+","-","/","*","%","+_REG","-_REG","/_REG","*_REG","%_REG","READ_MEM","WRITE_MEM","RET","CALL","JZ","JMP"
]
with open("code.bin","wb") as f:
    for line in code:
        split=line.split(" ")
        split+=["0"]*(3-len(split))
        f.write((opcode_table.index(split[0])+97).to_bytes()+int(split[1]).to_bytes(2)+int(split[2]).to_bytes(2))