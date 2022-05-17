import pandas as pd
from pandas import DataFrame
import csv
import statsmodels.api as sm
import sys
import numpy as np

# url https://www.kaggle.com/datasets/harsha547/indian-premier-league-csv-dataset


def run():
    args = list(sys.argv)
    if (len(args) < 2):
        print("File name require")
        sys.exit()
    if ("-h" in args):
        display_help()
        sys.exit()
    print(args[1])

    fname = args[1]
    read_csv(fname)
    get_averages(fname)
    sum_args(fname, args)
    read_data_from_csv(fname)

def get_averages(fname):
    readdata = csv.reader(open(fname, 'r'))  # this is the file you
    # ....will write your original file to....============
    data = []
    for row in readdata:
        data.append(row)
    Header = data[0]
    data.pop(0)
    q1 = []
    q2 = []

    for i in range(len(data)):
        if (data[i][10] == ' '):
            continue
        q1.append(int(data[i][10]))
        if (data[i][12] == ' '):
            continue
        q2.append(int(data[i][12]))
    print("================================ Batsman Score ================================")
    print('Mean:            ', (np.mean(q1)))
    print('Variance:          ', (np.sum(q1)))
    print('================================== Extra Runs =================================')
    print('Median:            ', (np.median(q2)))
    print('Average:          ', (np.average(q2)))
    print('================================================================================')

def read_data_from_csv(fname):
    if fname.endswith('.csv'):
        print("File format right and its opening")
    else:
        print("Wrong file format, Try Again")
        sys.exit()
    data = pd.read_csv(fname)
    print(data)
    print(data.head())
    print(data.describe())
    print("="*150)

    x = DataFrame(data, columns=['High'])
    y = DataFrame(data, columns=['Low'])

    model = sm.OLS(y, x).fit()
    print(model.summary())

# Task 5,6
def sum_args(fname, args):
    data = pd.read_csv(fname)
    model_w = data.groupby('Batsman_Scored', as_index=False).agg({"Batsman_Scored": "sum"})
    if("-o" in args):
        filename = str(args[3])
        print(f"Successfully created {filename} file")
        model_w.to_excel(filename)
    else:
        print("printing summary stats")
        model_w.to_excel('Nayem.xlsx')
        print(model_w)
        print(data.info())

# TASK 7
def display_help():
    print("+---------------------------------------HELP--------------------------------------------+")
    print("|                       Write python <filename>.csv to read file                        |")
    print("|           Write python <filename>.csv -o <filename> to generalte excel file           |")
    print("|                          Generated file name should end with xlsx                     |")
    print("|                   NB: File name must require and must be csv format                   |")
    print("+---------------------------------------------------------------------------------------+")


def read_csv(fname):
    with open(fname) as file:
        content = file.readlines()
    header = content[:1]
    rows = content[1:]
    print("+---------------------------------------All File Rows--------------------------------------------+")
    # print(rows)
    print("=" * 150)
    print(header)
    print("=" * 150)

    print("+---------------------------------------File Rows in Serial--------------------------------------------+")
    for i in range(10):
         print(rows[i])




if __name__ == "__main__":
    run()