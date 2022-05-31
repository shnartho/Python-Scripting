import json
import smtplib
from datetime import datetime
import argparse
import sys
import requests
from bs4 import BeautifulSoup
import re

def read_credentials():
    try:
        with open("personal_infos.json", 'r') as file:
            return json.loads(file.read())
    except Exception:
        print("Can't open personal_infos.json file, no such file or directory..")
        sys.exit(0)

def send_mail(mail_message, my_infos):
    smtSrv = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtSrv.starttls()
    smtSrv.ehlo()
    smtSrv.login(my_infos['e-mail'], my_infos['password'])
    print(f"Login Successful")


    Sender = my_infos["e-mail"]
    to ='shnartho@gmail.com'
    print(f"Sending email to {to}...... ")
    Subject_currenttime = f"Practicing smtp server {datetime.now().strftime('%H:%M:%S, %d/%m/%Y')}" #subject and datetime
    header_file = 'To:' + to + '\n' + 'From:' + Sender + '\n'
    message = f'{header_file}Subject: {Subject_currenttime}\n' \
              f'{mail_message}'
    result = smtSrv.sendmail(Sender, to, message)
    del message #deleting message for safety.
    if len(result) != 0:
        print(f"User did not receive mail {result}")
    print("Email has ben sent succesfully. Check inbox!")
    smtSrv.quit()

def cat_facts(value):
    r = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={value}'
    response = requests.get(r)
    parsed_response = (json.loads(response.text))

    if int(value) > 1:
        print(f"The {value} cat facts are:\n")
        for fact in parsed_response:
            print(f"{fact.get('text')}")
    elif int(value) == 1:
        print(parsed_response.get('text'))
    else:
        print("Error..")

def create_report(value):
    URL = requests.get(f'https://wefim.pwr.edu.pl/en/employees/wizytowki-pracownikow/page1.html?letter={value}')
    soup = BeautifulSoup(URL.text, 'html.parser')
    soup = soup.find_all('div', attrs={'class': 'col-text'})  # Finding the div
    newlist = []
    for line in soup:
        innerHTML = re.findall(r'(?<=>).+?(?=<)', str(line))  # Regex to find between '>'  and  '<' from the site inspect
        newlist.append(innerHTML)  # Putting info into lists
    if len(newlist) > 0:
        print(*newlist, sep='\n')
    else:
        print(f"There is no faculty lecturers with a last name starting with the: '{value}' letter!!")

def main():
    parser = argparse.ArgumentParser(description="Practice app")
    parser.add_argument('--mail', help="Sending an e-mail")
    parser.add_argument('--cat-facts', help="printing facts of cats", type=int)
    parser.add_argument('--teachers', help="printing information of researches")
    args = parser.parse_args()
    mail_message = args.mail

    my_infos = read_credentials()

    if mail_message:
        print('+' + 68 * '-' + 'Sending Email Using SMTP' + 68 * '-' + '+')
        send_mail(mail_message, my_infos)
        print('+' + 80 * '-' + 80 * '-' + '+')
    cat_facts_val = args.cat_facts
    if cat_facts_val:
        print('+' + 70 * '-' + 'Interesting Cat Facts' + 70 * '-' + '+')
        cat_facts(cat_facts_val)
        print('+' + 80 * '-' + 80 * '-' + '+')
    if args.teachers is not None:
        print('+'+70*'-'+ 'PWR Faculty Lecturers' +70*'-'+ '+')
        create_report(args.teachers)
        print('+' + 80 * '-' + 80 * '-' + '+')

if __name__ == '__main__':
    main()


