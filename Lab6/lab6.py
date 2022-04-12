import json
import sys
import logging


def run():
    print("-" * 150)
    print("Start")
    print("-" * 150)
    read_configuration()
    read_file = read_log()
    file_printer(read_file)
    print("-" * 150)
    set_logging_level()
    print("-" * 150)
    print_all_request(read_file)
    print_requests_according_to_config(read_file)
    searchEngine(read_file)


def read_configuration():
    filename = 'configuration.json'
    newDict = {}
    newDict1 = {}
    try:
        with open(filename) as json_file:
            newDict = json.load(json_file)
        print("Readed successfully")
    except OSError:
        print(f"OS error occurred trying to open {filename}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"file --{filename} does not exist")
    except ValueError:
        print(f"json file --{filename} is not correct")
    try:
        newDict1 = newDict.get("Name_Web_Server")
    except FileNotFoundError:
        print(f"logfile --{filename} with the given name does not exist (log error, display info about problem")

def read_log():
    new_dictionary = {}
    onlyIp = {}
    counter = 1
    with open('accesslog.txt', 'r') as file:
        for line in file:
            splitline = line.split()
            new_dictionary[''.join(splitline[:5])] = ''.join(splitline[5:])
            onlyIp[counter] = ''.join(splitline[0:1])
            counter += 1
        return new_dictionary

def file_printer(dict):
    for x in dict:
        print(str(x) + "     " + str(dict[x]))

def set_logging_level():
    newDict = {}
    ip = {}
    with open('configuration.json') as json_file:
        newDict = json.load(json_file)
        level = newDict.get("Logging_Level")
    if level == "DEBUG":
        logging.basicConfig(filename='logfile.log', filemode='w', level=logging.DEBUG)
        logging.debug("logging level is now set")
        print("logging level is now set")
    elif level == "INFO":
        logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO)
        logging.info("logging level is now set")
        print("logging level is now set")
    elif level == "ERROR":
        logging.basicConfig(filename='logfile.log', filemode='w', level=logging.ERROR)
        logging.error("logging level is now set")
        print("logging level is now set")
    elif level == "WARNING":
        logging.basicConfig(filename='logfile.log', filemode='w', level=logging.WARNING)
        logging.warning("logging level is now set")
        print("logging level is now set")
    elif level == "Critical":
        logging.basicConfig(filename='logfile.log', filemode='w', level=logging.CRITICAL)
        logging.critical("logging level is now set")
        print("logging level is now set")
    else:
        print(" Invalid Logging Level !!!")


def print_all_request(dict):
    newDict = {}
    ip = {}
    counter = 1
    with open('configuration.json') as json_file:
        newDict = json.load(json_file)
        ip = newDict.get("Ip_Address")
    for x in dict:
        if ip in x:
            print(str(counter)+ " " + str(ip) +" Ip found in request:"+ x + " ------ " + dict[x])
            counter += 1
    assert counter != 1, "No match found!"
    assert counter != 1187, "Please Input IP in correct order!"

def print_requests_according_to_config(d):
    http_method = []
    counter = 0
    for x in d.values():
        http = x[4].split(" ")[0]
        if http == http_method:
            print(x)
            counter += 1

def searchEngine(dict):
    newDict = {}
    web = {}
    counter = 1
    with open('configuration.json') as json_file:
        newDict = json.load(json_file)
        web = newDict.get("Name")
    for x in dict:
        if web in dict[x]:
            print(str(counter) +" "+ str(web) +" search engine found in request:" + x + " ------ " + dict[x])
            counter += 1

    assert counter != 1, "No match found!"
    assert counter != 1187, "Wrong input, please write in proper format eg. www.google.com!"


if __name__ == "__main__":
    run()