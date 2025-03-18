import string

secret_cheese=input("Enter encrypted cheese >")
babybel_encrypted=input("encrypted text of BABYBEL >")
a=ord(babybel_encrypted[0])-ord(babybel_encrypted[1])
b=ord(babybel_encrypted[1])
data={}
for c in " "+string.ascii_uppercase:
    data[chr(
        (a*ord(c)+b)%26+ord("A")
    )]=c

print("".join([data[t] for t in secret_cheese]))