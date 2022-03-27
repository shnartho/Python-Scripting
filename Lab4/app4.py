import ipaddress
import logging
from datetime import datetime, timedelta
import time



def run():
    logging.basicConfig(filename='report.log', filemode='w', level=logging.DEBUG)
    logging.info("App4.py has Started")
    print("Checking IP address:")
    checkIpAddress()
    Logfile = read_log()

    print("\nStandard date time format:")
    datetimelist = dateTimeSplitter(Logfile)
    dateTimeFunction(str(datetimelist[0]))

    print("\nClass object:")
    objectLog1 = Logentry("190.192.13.1", "08/07/2020:00:09:07", "/index.html", 200)
    logging.warning("Html code is an int")
    print(type(objectLog1.htmlCode))
    objectLog1.convertIntoString()
    print(repr(objectLog1))
    logging.debug("All arg from objectLog1 converted to string")

    print("\nLog entry object:")
    txt = "152.32.65.99 18/Oct/2020:00:15:28 /robots.txt 200 343 2"
    objectLog2 = logEntryObject(txt)
    print(repr(objectLog2))


    print("\nLog entry Objects:")
    objectLog = logEntryObjects(Logfile)
    for obj in objectLog:
        print(obj.IPadress, obj.date, obj.resourceFile, obj.htmlCode ,sep=' ')

    print("\nTasks between given time:")
    startTime = input("Start time:")
    endTime = input("End time:")
    taskBetweenTime(startTime, endTime)

    print(pythonDocumentation.__doc__)

def checkIpAddress():
    checkip = ipaddress.ip_address('192.168.0.1') in ipaddress.ip_network('192.168.0.0/24')
    if checkip == True:
        print("IPv4 address 192.168.0.1 belongs to IPv4 Network 192.168.0.0/24")

def dateTimeFunction(timestamp):
    newDate = timestamp.split(':')
    newDate1 = ':'.join(newDate[1:])
    newDate2 = ' '.join(newDate[:1])
    newDate3 = newDate2 +" "+newDate1

    standard_date_obj = datetime.strptime(newDate3, '%d/%b/%Y %H:%M:%S')
    print(standard_date_obj)
    return  standard_date_obj


def dateTimeSplitter(file):
    splitline = []
    datetimelist = []
    for line in file:
        splitline = line.split()[1]
        datetimelist.append(splitline)
    return datetimelist

class Logentry:
    def __init__(self, IPaddress, date, resourceFile, htmlCode):
        self.IPadress = IPaddress
        self.date = date
        self.resourceFile = resourceFile
        self.htmlCode = htmlCode

    def convertIntoString(self):
        strIPadress = str(self.IPadress)
        strdate = str(self.date)
        strresourceFile = str(self.resourceFile)
        strhtmlCode = str(self.htmlCode)
        print("%s %s %s %s" % (strIPadress, strdate, strresourceFile, strhtmlCode))

    def showSeparately(self):
        print("IP: %s \nDate: %s\nResource file: %s\nHtml code: %s" % (self.IPadress, self.date, self.resourceFile, self.htmlCode))
    def show(self):
        print("%s %s %s %s" % (self.IPadress, self.date, self.resourceFile, self.htmlCode))

    def __repr__(self):
        rep = 'Representing instances:\n Ipaddress:' + str(self.IPadress) + ' Date:' + str(self.date) + ' Resource file: '+ str(self.resourceFile) +' Html code:'+ str(self.htmlCode)
        return rep

def logEntryObject(firstline):
    splitline = firstline.split()
    html = ' '.join(splitline[3:])
    newobject = Logentry(splitline[0], splitline[1], splitline[2], html)
    return newobject

def logEntryObjects(file):
    listOfObjects = []
    splitline = []
    for line in file:
        splitline = line.split()
        html = ' '.join(splitline[3:])
        listOfObjects.append(Logentry(splitline[0], splitline[1], splitline[2], html))


    return listOfObjects

def taskBetweenTime(starttime, endtime):
    time.sleep(int(starttime))
    delta1 = timedelta(seconds=int(starttime))
    print("This printing request has been executed after %d Seconds" % (int(starttime)))
    delta2 = timedelta(minutes=int(endtime))
    delta3 = delta2-delta1
    print(delta3)


def read_log():
    readLogFile = []
    with open('accesslog4.txt', 'r') as file:
        for line in file:
            readLogFile.append(line)
    return readLogFile

def pythonDocumentation():
    '''
    IPaddress documentation: https://docs.python.org/3/library/ipaddress.html
    Datetime documention: https://docs.python.org/3/library/datetime.html

    '''

if __name__ == '__main__':
    run()

