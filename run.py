__author__ = 'prithvin'

import numpy as np
from input_reader import read_tube_quotes
from linear_reg import Predictor


def run():
    tube_quotes = filter(lambda x: x.supplier == 'S-0041', read_tube_quotes())
    features = np.array(map(lambda x: x.features(), tube_quotes), dtype='float_')
    output = np.array(map(lambda x: [x.cost], tube_quotes), dtype='float_')
    predictor = Predictor(features, output)
    predictor.fit()

    tube = tube_quotes[10]
    print "predicting for assembly id ", tube.tube.assembly_id, ' with features ', tube.features()
    print 'The million dollar prediction is ', predictor.predict(np.array(tube.features(), dtype='float'))


if __name__ == '__main__':
    run()