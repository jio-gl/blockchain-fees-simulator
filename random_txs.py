
from txs import AbstractTransactions
from base import Tx


from scipy.stats import skewnorm
import random


class RandomTransactions(AbstractTransactions):

    def __init__(self, skewness=4, average_price=None, min_gas_price=1, max_gas_price=None,
                 block_gas_size=None, txs_per_block=None, block_time=None):
        self.skewness = skewness
        self.average_price = average_price
        self.min_gas_price = min_gas_price
        self.max_gas_price = max_gas_price
        self.block_gas_size = block_gas_size
        self.txs_per_block = txs_per_block
        assert( self.block_gas_size >= self.txs_per_block )
        self.block_time = block_time

    def next_transaction(self):
        # price
        rand_delta = skewnorm.rvs(self.skewness, size=1)[0]
        price = self.average_price * (rand_delta + 1)
        price = max(self.min_gas_price, price)
        if self.max_gas_price:
           price = min(self.max_gas_price, price)
        # gas consumed
        # 1 <= gas_consumed <= 2* block_size / txs_per_block
        gas = random.randint(1, 2*int(self.block_gas_size/self.txs_per_block))
        return Tx(gas, price)

    def next_wait_time_ms(self):
        return random.uniform( 0, self.block_time / self.txs_per_block )
