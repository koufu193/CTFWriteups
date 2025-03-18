from hashlib import sha256
cheese_list=open("cheese_list.txt").read().splitlines()
def crack(_hash):
    for cheese in cheese_list:
        for salt in range(256):
            if sha256(cheese.lower().encode()+salt.to_bytes()).hexdigest()==_hash:
                return cheese.lower(),salt.to_bytes().hex()
    return None
while True:
    _hash=input("Enter your hash >")
    cracked=crack(_hash)
    if not cracked:
        print("Not found")
        continue
    cheese,salt=cracked
    print(f"cheese:{cheese}")
    print(f"salt:{salt}")