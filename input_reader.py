import csv
from tube import TubeQuote

__author__ = 'prithvin'


def get_quantity(row):
    if row['bracket_pricing'] == 'yes':
        return row['quantity']
    else:
        return row['min_order_quantity']


def read_tube():
    with open('../data/competition_data/train_set.csv', 'r') as train_file:
        reader = csv.DictReader(train_file)
        tube_quotes = []
        for row in reader:
            tube_quotes.append(
                TubeQuote(row['tube_assembly_id'], row['supplier'], row['quote_date'], row['annual_usage'], row['cost'],
                          get_quantity(row)))

        print tube_quotes

read_tube()