


class Store(object):
    def __init__(self, name_product, price_product):
        self.name_product = name_product
        self.price_product = price_product

    def to_json1(self):
        return {'name_product': self.name_product, 'price_product': self.price_product}

    #@staticmethod
    @classmethod
    def from_json1(cls, js_object):
        return cls(js_object['name_product'], js_object['price_product'])
    
    def __repr__(self):
        #print('Hello111')
        return '|Product: {name_product!r}| price: {price_product!r}|'.format_map(self.__dict__)

