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

    fig = plt.figure()
    ax = Axes3D(fig)
    # ax.plot(xs=x_values, ys=y_values, zs=z_values, marker='o', ls='None')
    ax.scatter3D(xs=x_values, ys=y_values, zs=z_values)
    ax.set_xlabel('Quantity of Tubes Purchased')
    ax.set_ylabel('Tube Diameter')
    ax.set_zlabel('Tube Cost')

    plt.show()

main()