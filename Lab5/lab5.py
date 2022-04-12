import logging
import json

def run():
    print("-" * 150)
    print("Start")
    print("-" * 150)
    newDictionary, onlyIp = read_log()
    file_printer(newDictionary)
    print("-" * 150)
    print("-" * 150)
    ipDictionary = ip_request(newDictionary)
    print("Number of requests: ", ipDictionary)
    print("-" * 150)
    print("-" * 150)
    print("Biggest request ip address is ",ip_find(onlyIp, True))
    # print("Least Frequent is ", ip_find(ipDictionary, False))
    print(longest_request(newDictionary))
    print(non_existent(newDictionary))

def file_printer(dict):
    for x in dict:
        print(str(x) + "     " + str(dict[x]))

def ip_request(dict):
    ips = {}
    for x in dict:
        ip = x.split()
        ipKey = 0
        ips[ipKey] = ips.get(ipKey, 0) + 1
    return ips

def longest_request(dict):
    max = 0
    ip = {}
    lon_req = {}
    for x in dict:
        if len(x) > max:
            ip = x.split()
            max = len(x)
            lon_req = x
            lon_req = { "IP of the longest request": ip,"Max length": max}
    return lon_req


def non_existent(dict):
    non_ex = []
    print("-"*150)
    print("+++++++     404     +++++++")
    print("-" * 150)
    for x in dict:
        http_code = dict[x]
        newVal = http_code.find("404")
        if newVal >= 0:
            if http_code not in non_ex:
                non_ex.append(http_code)
    non_ex = '\n'.join(non_ex)
    return non_ex

def ip_find(ipDict, most_active: bool=False):
    ips = list(ipDict.values())
    if most_active == True:
        dict = {}
        count, itm = 0, ''
        for item in reversed(ips):
            dict[item] = dict.get(item, 0) + 1
            if dict[item] >= count:
                count, itm = dict[item], item
        return itm

    elif most_active == False:
        counter = 0
        small_req = ips[counter]
        lenth = len(ips)
        for i in range(lenth):
            for x in ips:
                if x not in small_req:
                    continue
                else:
                    break

        return small_req






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
        return new_dictionary, onlyIp

if __name__ == "__main__":
    run()