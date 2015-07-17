__author__ = 'prithvin'
import csv


def main():
    with open('../data/competition_data/train_set.csv', 'r') as train_file:
        reader = csv.reader(train_file)
        for row in reader:
            print(row[01])
