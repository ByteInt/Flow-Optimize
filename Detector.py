# Getting result from the inline IR
# Serial number might be needed from Mettler Torendo service

import csv

reader = csv.reader(open('C:/Users/z1445/Desktop/exp.csv', 'r'))

for row in reader:
    print(row)

print()


def detect():
    return 0


# Ask JW to turn on the inline IR machine and see what the csv file look like.
