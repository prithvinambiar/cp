import csv

from tube import TubeQuote, Tube


__author__ = 'prithvin'


def _get_quantity_(row):
    if row['bracket_pricing'] == 'yes':
        return row['quantity']
    else:
        return row['min_order_quantity']


def is_bracket_pricing(row):
    return 1 if row['bracket_pricing'] == "yes" else 0


def read_tube_quotes():
    with open('../data/competition_data/temp/tube.csv', 'r') as tube_file:
        tube_reader = csv.DictReader(tube_file)
        tubes = {}
        for row in tube_reader:
            tubes[row['tube_assembly_id']] = Tube(row['tube_assembly_id'], row['material_id'], float(row['diameter']),
                                                  float(row['wall']), float(row['length']),
                                                  float(row['num_bends']), float(row['bend_radius']))

    print 'Number of tubes ', len(tubes)

    with open('../data/competition_data/temp/train_set.csv', 'r') as train_file:
        train_reader = csv.DictReader(train_file)

        tube_quotes = []
        for row in train_reader:
            tube = tubes[row['tube_assembly_id']]
            tube_quotes.append(
                TubeQuote(tube, row['supplier'], row['quote_date'], float(row['annual_usage']), float(row['cost']),
                          float(row['quantity']), is_bracket_pricing(row)))

        print 'Number of tube quotes ', len(tube_quotes)
        return tube_quotes