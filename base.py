
class Tx:

    def __init__(self, gas_consumed, gas_price):
        self.gas_consumed = gas_consumed
        self.gas_price =  gas_price

    def __repr__(self):
        return '<gas_consumed=%d,gasprice=%d>' % (self.gas_consumed,self.gas_price)


class Block:

    def __init__(self, max_gas_size, tx_iterable=None):
        if not tx_iterable:
            tx_iterable = []
        self.max_gas_size = max_gas_size
        self.block = list(tx_iterable)
        self.block.sort(key=lambda x: x.gas_price)

    def is_too_big(self):
        gas_size = sum([tx.gas_consumed for tx in self.block])
        return gas_size > self.max_gas_size

    def __len__(self):
        return len(self.block)

    def min_gas_tx(self):
        return self.block[0]

    def max_gas_tx(self):
        return self.block[-1]

    def remove_max_gas_tx(self):
        self.block = self.block[:-1]

    def remove_min_gas_tx(self):
        self.block = self.block[1:]

    def can_add_tx_size(self, tx):
        self.block.append(tx)
        ret = not self.is_too_big()
        self.block = self.block[:-1]
        return ret

    def add_tx(self, tx):
        self.block.append(tx)
        self.block.sort(key=lambda x: x.gas_price)

    def total_gas(self):
        return sum([tx.gas_consumed for tx in self.block])


