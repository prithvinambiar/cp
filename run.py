from input_reader import read_tube_quotes

__author__ = 'prithvin'
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    tube_quotes = read_tube_quotes()
    tube_quotes = filter(lambda x: x.supplier == 'S-0041', tube_quotes)
    tube_quotes = filter(lambda x: float(x.quote_date.split('/')[2]) > 2010, tube_quotes)

    print 'number of tubes ', len(tube_quotes)
    z_values = map(lambda x: float(x.cost), tube_quotes)
    x_values = map(lambda x: float(x.quantity), tube_quotes)
    y_values = map(lambda x: float(x.tube.diameter), tube_quotes)

    # plt.plot(y_values, x_values, 'ro')

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x_values, y_values, z_values, 'ro')
    plt.show()

main()