import base64

import requests
import email.message

URL="http://activist-birds.picoctf.net:64542"
def login():
    password=requests.get(f"{URL}/api/password").json()
    print(f"{password=}")
    token=requests.post(f"{URL}/api/login",json={"username":"user@ses","password":password}).json()
    print(f"{token=}")
    return token

def get_emails(token):
    return requests.get(f"{URL}/api/emails",headers={"Token":token}).json()

def send_email(to,subject,body,token):
    return requests.post(f"{URL}/api/send",json={"to":to,"subject":subject,"body":body},headers={"Token":token}).json()

def admin_bot(token):
    print(requests.post(f"{URL}/api/admin_bot",headers={"Token":token}).json())

def get_email(i,token):
    return requests.get(f"{URL}/api/email/{i}", headers={"Token": token}).json()