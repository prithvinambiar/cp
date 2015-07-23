__author__ = 'prithvin'


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
    def __init__(self, tube, supplier, quote_date, annual_usage, cost, quantity):
        self.quantity = quantity
        self.cost = cost
        self.annual_usage = annual_usage
        self.quote_date = quote_date
        self.supplier = supplier
        self.tube = tube