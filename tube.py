__author__ = 'prithvin'


class TubeQuote:
    def __init__(self, assembly_id, supplier, quote_date, annual_usage, cost, quantity):
        self.quantity = quantity
        self.cost = cost
        self.annual_usage = annual_usage
        self.quote_date = quote_date
        self.supplier = supplier
        self.assembly_id = assembly_id

