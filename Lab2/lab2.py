# import fileinput
#
# with fileinput.input(files=('log.txt')) as f:
#     for line in f:
#         print(line)
#   -------------------------
# import sys
#
# for line in sys.stdin:
#     print(line)

import fileinput
import logging
import time

start_time = time.time()
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(message)s',
#                     handlers=[logging.FileHandler("example1.log"),
#                               logging.StreamHandler()])

logging.basicConfig(filename='lab2.log',filemode='w',level=logging.ERROR,
                    format='%(asctime)s %(message)s')
#logging.disable()
logging.info("Application is launching")


for f in fileinput.input():
    print(f.split())

string1 = '404'
file1 = open("log.txt", "r")
flag = 0
index = 0
for line in file1:
    index += 1
    if string1 in line:
        flag = 1
        break
if flag == 0:
    print('Code', string1, 'Not Found')
else:
    print('Code', string1, 'Found In Line', index)
file1.close()


logging.warning("404 detected in line 2")
file1 = open('log.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if count == 2:
        print("Line{}:!{}".format(count, line.strip()))
    else:
        print("Line{}: {}".format(count, line.strip()))

name = 'Nayem'
logging.error('%s raised an error', name)

print("---Total Time: %s seconds ---" % (time.time() - start_time))






