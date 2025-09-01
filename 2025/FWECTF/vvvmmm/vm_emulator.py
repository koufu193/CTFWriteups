import sys
code=open("code.txt").read().splitlines()
memory=[0]*0x1000
call_stack=[]
ip=0x1000-1
sp=0x1000-2
while memory[ip]<len(code):
    #print(memory[ip],code[memory[ip]])
    inst=code[memory[ip]].split(" ")
    memory[ip]+=1
    match inst[0]:
        case "READ":
            memory[0]=ord(sys.stdin.read(1)[0])
        case "PUTC":
            print(chr(memory[0]),end="")
        case "MOV":
            #MOV REG_ID NUM
            memory[int(inst[1])]=int(inst[2])
        case "PUSH":
            #PUSH NUM
            memory[memory[sp]] = int(inst[1])
            memory[sp]+=1
        case "PUSH_REG":
            #PUSH REG_ID
            memory[memory[sp]] = memory[int(inst[1])]
            memory[sp]+=1
        case "POP":
            #POP REG_ID
            memory[sp]-=1
            memory[int(inst[1])]=memory[memory[sp]]
        case "READ_MEM":
            #print("READ",memory[int(inst[1])])
            memory[int(inst[1])]=memory[memory[int(inst[1])]]
        case "WRITE_MEM":
            #print("WRITE", memory[int(inst[1])],memory[int(inst[2])])
            memory[memory[int(inst[1])]]=memory[int(inst[2])]
        case "MOV_REG":
            #MOV_REG REG_ID REG_ID
            memory[int(inst[1])] = memory[int(inst[2])]
        case "+_REG":
            memory[int(inst[1])] += memory[int(inst[2])]
        case "-_REG":
            memory[int(inst[1])] -= memory[int(inst[2])]
        case "*_REG":
            memory[int(inst[1])] *= memory[int(inst[2])]
        case "/_REG":
            assert memory[int(inst[2])]!=0
            memory[int(inst[1])] //= memory[int(inst[2])]
        case "%_REG":
            assert memory[int(inst[1])]!=0
            memory[int(inst[1])] %= memory[int(inst[2])]
        case "+":
            memory[int(inst[1])]+=int(inst[2])
        case "-":
            memory[int(inst[1])] -= int(inst[2])
        case "*":
            memory[int(inst[1])] *= int(inst[2])
        case "/":
            assert int(inst[2])!=0
            memory[int(inst[1])] //= int(inst[2])
        case "%":
            assert int(inst[1])!=0
            memory[int(inst[1])] %= int(inst[2])
        case "RET":
            if len(call_stack)==0:
                break
            memory[ip]=call_stack.pop()
            continue
        case "CALL":
            call_stack.append(memory[ip])
            memory[ip]=int(inst[1])
            continue
        case "JZ":
            if memory[int(inst[1])]==0:
                memory[ip]=int(inst[2])
                continue
        case "JMP":
            memory[ip]=int(inst[1])
            continue
        case _:
            print("Invalid Instruction:",inst)
            break