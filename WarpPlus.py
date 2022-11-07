import random
import string
import requests
import datetime
import json
import os
import time
import alive_progress

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)

def send_request(referrer):
    try:
        url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
        r = requests.session()
        print(f"[+] Account ID : {referrer}")
        print("[*] Creating request Body")
        install_id = genString(22)
        body = {
                "key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Host': 'api.cloudflareclient.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.12.1'
        }
        print("[*] Sending Request ...")
        res = r.post(url=url,headers=headers,data=data)
        if res.status_code == 200:
            print("[+] Sent | 1 GB has been successfully added to your account.")
    except Exception as error:
        print(f"[-] {error}")
Total = 0
def run(Total):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        referrer = input("[~] Enter ID : ")
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                send_request(referrer)
                Total += 1
                print(f"[+] Total Gigabytes : {Total} | Github : IR4N14N")
                with alive_progress.alive_bar(100, ctrl_c=True, title=f'[+] Waiting 20 seconds before sending request') as bar:
                    for i in range(100):
                        time.sleep(0.2)
                        bar()
            except KeyboardInterrupt:
                print("[-] Closing...")
                exit()
    except KeyboardInterrupt:
        print("Closing ...")
        exit()

run(Total)
