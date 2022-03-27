import sys
import fileinput
import os
import os.path
import logging

def run():
    logging.basicConfig(filename='report.log', filemode='w', level= logging.DEBUG)
    logging.info("Project Start")
    print("\n\n Task4 \n\n")
    readedFile, sliceFile = read_log()
    printDictionary(sliceFile)

    myTuple = tupleFunc(readedFile)
    print(myTuple)

    print("\nList of Succesful Reads:")
    list_SuccesfulReads = successful_reads(readedFile)
    print(list_SuccesfulReads)

    print("\nList of Failed Reads:")
    list_FailedReads = failed_reads(readedFile)
    print(list_FailedReads)

    print("\nList of HTML entries:")
    # listOfHtmlEntries = html_entries(readedFile)
    # print(listOfHtmlEntries)

    newHtmlList = html_entries(readedFile)
    print_html_entries(newHtmlList)



def printDictionary(dictionary):

    for x in dictionary:
        print("Resource Name:"+ str(x) + ", HTML CODE:" + str(dictionary[x]))



def read_log():
    new_dictionary = {}
    newList = []
    numberOfLines = 0
    splt_char = ' '
    with open('log.txt', 'r') as f:
        for line in f:
            splitline = line.split()
            newList.append(line)
            numberOfLines += 1
            logging.warning("line splitted")
            new_dictionary[splt_char.join(splitline[:1])] = splt_char.join(splitline[1:])

        logging.debug("Number of Lines: %d", numberOfLines)
        return newList,new_dictionary

def tupleFunc(file):
    myTuple = []
    for line in file:
        myTuple.append(tuple(line.replace('\n', ' ').split('\t')))
    return myTuple

def successful_reads(file):
    newOkayList = []
    countFor200 = 0
    for line in file:
        if '200' in line:
            newOkayList.append(line)
            countFor200 += 1
    logging.info("Entries with 200: %d", countFor200)
    return newOkayList

def failed_reads(file):
    failedList = []
    newFailedList1 = []
    newFailedList2 = []
    countFor404 = 0
    countFor500 = 0
    for line in file:
        if '404' in line:
            newFailedList1.append(line)
            countFor404 += 1

    for line in file:
        if '500' in line:
            newFailedList2.append(line)
            countFor500 += 1
    logging.info("Entries with 404: %d and Entries with 500: %d", countFor404, countFor500)
    logging.info("Merging failed lists")
    failedList = newFailedList1 + newFailedList2
    return failedList

def html_entries_fromdir():
    path = "/home/shnartho/Erusmus Semester 2/Script Language/Lab3"
    for i in os.listdir(path):
        # List files with .html
        if i.endswith(".html"):
            print("Files with extension .py are:", i)

def html_entries(file):
    list_html = []
    for line in file:
        if '.html' in line and '200' in line:
            list_html.append(line)
        # extension = os.path.splitext(line)[1]
        # print(extension)
    return list_html

def print_html_entries(list):
    for x in list:
        logging.info("printing html entries")
        print("Retrieved page:  " + str(x))


if __name__ == "__main__":
    run()