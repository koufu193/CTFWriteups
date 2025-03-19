# Quantum Scrambler
> We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?<br>
> Connect to the program with netcat:<br>
> $ nc SERVER PORT<br>
> The program's source code can be downloaded here.

```python:quantum_scrambler.py
import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
    
  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()
```
入力に対して出力が一意に定まりそうなのでフラグの長さの総当たり+[["0"],["1"],["2"],...]をscrambleに渡した結果を比べて解く。