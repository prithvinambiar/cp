import csv
import time

from tube import TubeQuote, Tube


__author__ = 'prithvin'


def _get_quantity_(row):
    if row['bracket_pricing'] == 'yes':
        return row['quantity']
    else:
        return row['min_order_quantity']


def read_tube_quotes():
    with open('../data/competition_data/tube.csv', 'r') as tube_file:
        tube_reader = csv.DictReader(tube_file)
        tubes = []
        for row in tube_reader:
            tubes.append(Tube(row['tube_assembly_id'], row['material_id'], row['diameter'], row['wall'], row['length'],
                              row['num_bends'], row['bend_radius']))

    print 'Number of tubes ', len(tubes)

    with open('../data/competition_data/train_set.csv', 'r') as train_file:
        train_reader = csv.DictReader(train_file)

        start_time = time.time()
        tube_quotes = []
        for row in train_reader:
            tube = next(x for x in tubes if x.assembly_id == row['tube_assembly_id'])
            tube_quotes.append(
                TubeQuote(tube, row['supplier'], row['quote_date'], row['annual_usage'], row['cost'],
                          _get_quantity_(row)))

        end_time = time.time()
        print 'Number of tube quotes ', len(tube_quotes)
        print 'Time taken to populate all tube quotes is ', end_time - start_time, ' seconds!!!!'
        return tube_quotes