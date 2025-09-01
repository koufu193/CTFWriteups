import random
import marshal
from class_definition import *
import sys
arr=['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',"__builtins__","kokoni___builtins___ga_arimasu" 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',"get", 'compile', 'complex', 'copyright',"join", 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip',"__builtins__kara_copy_simasita","Yokumitsuketane!","Hazimeteno_rev_sakumonn_dakara_soutei_ijoni_kantan_kamo_(sirankedo)","Debugger_bougai_tte_douyarunoga_iinndaro"]
chr_s=f"A%{arr.index('chr')}"
map_s=f"A%{arr.index('map')}"
join_s=f"A%{arr.index('join')}"
str_s=f"A%{arr.index('str')}"
bytes_s=f"A%{arr.index('bytes')}"
settattr_s=f"A%{arr.index('setattr')}"
def bytes_to_arr(b):
    b=b[::-1]
    res=f"(t-{str(b[0])})"
    for i in range(1,len(b)):
        res+=f"*{str(b[i]-b[i-1])}"
    return f"{res}//{len(b)}"
def fast_str(s):
    s=s[::-1]
    res=""
    i=0
    l=0
    while i<len(s):
        l+=1
        t=random.randint(1,3)+i
        t=min(t,len(s))
        res+=f"-{repr(s[i:t][::-1])}"
        i=t
    return res,l
def r():
    return random.randint(0,255)
class Gen:
    def __init__(self):
        self.code="t"
    def push_str(self,s):
        self.code+=f'-(-((((({bytes_to_arr(s.encode())}-{chr_s})**{r()}-{map_s})**{r()}^2)-""-{join_s}-{str_s})**{r()}%1^2))'
    def push_str_fast(self,s):
        a,b=fast_str(s)
        self.code=f"(({self.code}{a})/{b})"
    def push_int(self,i):
        self.code=f"({self.code}-{i})"
    def push_bytes(self,s):
        self.code+=f'-(-((({bytes_to_arr(s)}-{bytes_s})**{r()})^1))'
    def push_int_arr(self,arr):
        self.code+= f"-(-({bytes_to_arr(arr)}))"
    def call(self,args_len):
        self.code=f"({self.code}^{args_len})"
    def pop(self):
        self.code=f"(-({self.code}))"
    def get_from_builtins(self):
        self.code=f"(({self.code})**{r()})"
    def getattr(self):
        self.code=f"(({self.code})%1)"
    def setattr(self): #obj,name,data
        self.code=f"(({self.code}-{settattr_s})**{r()}^3)"
    def append(self,t):
        self.code=f"({self.code}*{repr(t)})"
    def make_array(self,n):
        self.code=f"({self.code}//{n})"

def read_flag():
    g=Gen()
    g.push_str("Enter your flag:")
    g.push_str("input")
    g.get_from_builtins()
    g.call(1)
    g.push_str("encode")
    g.push_str_fast("str")
    g.get_from_builtins()
    g.getattr()
    g.call(1)
    return g.code
def return_back():
    g=Gen()
    g.push_int("b")
    g.pop()
    return g.code
def init_random():
    g=Gen()
    g.append(b"")
    g.push_str("sum")
    g.get_from_builtins()
    g.call(1)
    g.push_str("seed")
    g.push_str("random")
    g.push_str("__import__")
    g.get_from_builtins()
    g.call(1)
    g.getattr()
    g.call(1)
    g.push_str(f"lambda a,b:{return_back()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.call(2)
    return g.code
def generate_key():
    g=Gen()
    g.push_int(255)
    g.push_int(0)
    g.push_str("randint")
    g.push_str("random")
    g.push_str("__import__")
    g.get_from_builtins()
    g.call(1)
    g.getattr()
    g.call(2)
    g.pop()
    return g.code
def generate_keys():
    g=Gen()
    g.push_int(49)
    g.push_int(0)
    g.push_str("range")
    g.get_from_builtins()
    g.call(2)
    g.push_str(f"lambda _:{generate_key()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.push_str("map")
    g.get_from_builtins()
    g.call(2)
    g.push_str("list")
    g.get_from_builtins()
    g.call(1)
    g.pop()
    return g.code
def incorrect():
    g=Gen()
    g.push_str("Incorrect")
    g.push_str("print")
    g.get_from_builtins()
    g.call(1)
    g.push_str("exit")
    g.get_from_builtins()
    g.call(0)
    g.call(284)
    return g.code
def correct():
    g=Gen()
    g.push_str("Correct!")
    g.push_str("print")
    g.get_from_builtins()
    g.call(1)
    g.push_str("exit")
    g.get_from_builtins()
    g.call(0)
    g.call(284)
    return g.code
def check_len():
    g=Gen()
    g.append(b"")
    g.push_str("len")
    g.get_from_builtins()
    g.call(1)
    g.push_str("__eq__")
    g.push_int(49)
    g.getattr()
    g.call(1)
    g.push_str("__getitem__")
    g.push_str(f'lambda:{generate_keys()}')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.push_str(f'lambda:{incorrect()}')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.make_array(2)
    g.getattr()
    g.call(1)
    g.call(0)

    #__builtins__.update(print=lambda a:exec("while True:\\n\\texit()"))
    return g.code
def encrypt_char(): #input a,b
    g=Gen()
    g.push_int("a")
    g.push_str("__xor__")
    g.push_int("b")
    g.getattr()
    g.call(1)
    g.pop()
    return g.code
def encrypt_flag():
    g=Gen()
    g.push_str(f'lambda:[{encrypt_char()} for a,b in zip(-t,-t)]')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.call(0)
    g.push_str("__eq__")
    g.push_int_arr([145, 233, 148, 144, 2, 16, 109, 230, 148, 219, 171, 255, 113, 14, 128, 224, 141, 88, 73, 85, 215, 93, 55, 104, 126, 135, 209, 154, 99, 229, 155, 250, 172, 252, 102, 29, 73, 25, 248, 47, 184, 126, 153, 187, 31, 72, 21, 236, 141])
    g.getattr()
    g.call(1)
    g.push_str("__getitem__")
    g.push_str(f"lambda :{correct()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.push_str(f"lambda :{incorrect()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.make_array(2)
    g.getattr()
    g.call(1)
    g.call(0)

    return g.code
def one_code():
    g = Gen()
    g.push_str("Enter your flag:")
    g.push_str("input")
    g.get_from_builtins()
    g.call(1)
    g.push_str("encode")
    g.push_str_fast("str")
    g.get_from_builtins()
    g.getattr()
    g.call(1)

    g.append(b"")
    g.push_str("sum")
    g.get_from_builtins()
    g.call(1)
    g.push_str("seed")
    g.push_str("random")
    g.push_str("__import__")
    g.get_from_builtins()
    g.call(1)
    g.getattr()
    g.call(1)
    g.push_str(f"lambda a,b:{return_back()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.call(2)

    g.append(b"")
    g.push_str("len")
    g.get_from_builtins()
    g.call(1)
    g.push_str("__eq__")
    g.push_int(49)
    g.getattr()
    g.call(1)

    g.push_str("__and__")
    g.push_bytes(b"fwectf")
    g.push_str("startswith")
    g.push_str("lambda:t.A[-5]")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.call(0)
    g.getattr()
    g.call(1)
    g.getattr()
    g.call(1)

    g.push_str("__getitem__")
    g.push_str(f'lambda:{generate_keys()}')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.push_str(f'lambda:{incorrect()}')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.make_array(2)
    g.getattr()
    g.call(1)
    g.call(0)

    g.push_str(f'lambda:[{encrypt_char()} for a,b in zip(-t,-t)]')
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.call(0)
    g.push_str("__eq__")
    g.push_int_arr([145, 233, 148, 144, 2, 16, 109, 230, 148, 219, 171, 255, 113, 14, 128, 224, 141, 88, 73, 85, 215, 93, 55, 104, 126, 135, 209, 154, 99, 229, 155, 250, 172, 252, 102, 29, 73, 25, 248, 47, 184, 126, 153, 187, 31, 72, 21, 236, 141])
    g.getattr()
    g.call(1)
    g.push_str("__getitem__")
    g.push_str(f"lambda :{correct()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.push_str(f"lambda :{incorrect()}")
    g.push_str("eval")
    g.get_from_builtins()
    g.call(1)
    g.make_array(2)
    g.getattr()
    g.call(1)
    g.call(0)
    return g.code
"""
encrypt
"""
"""
test([
    read_flag(),
    init_random(),
    check_len(),
    encrypt_flag(),

])
"""
#test([one_code()])
#g=Gen()
#g.push_str_fast("Enter your flag")
#test(g.code)
with open("main.py","w") as f:
    f.writelines([
        open("class_definition.py").read(),
        one_code()
    ])