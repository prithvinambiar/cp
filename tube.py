__author__ = 'prithvin'

import time

from dateutil import parser


class Tube:
    def __init__(self, assembly_id, material_id, diameter, wall, length, num_bends, bend_radius):
        self.bend_radius = bend_radius
        self.num_bends = num_bends
        self.length = length
        self.wall = wall
        self.diameter = diameter
        self.material_id = material_id
        self.assembly_id = assembly_id


class TubeQuote:
    def __init__(self, tube, supplier, quote_date, annual_usage, cost, quantity, is_bracket_pricing):
        self.quantity = quantity
        self.cost = cost
        self.annual_usage = annual_usage
        self.quote_date = quote_date
        self.supplier = supplier
        self.tube = tube
        self.is_bracket_pricing = is_bracket_pricing

    def quote_date(self):
        date = parser.parse(self.quote_date)
        return time.mktime(date.timetuple())

    def features(self):
        tube = self.tube
        return [self.quantity, self.annual_usage, tube.bend_radius, tube.diameter, tube.length, tube.num_bends,
                tube.wall, self.is_bracket_pricing, self.quantity ** 2, self.quantity ** 3, self.quantity ** 4]