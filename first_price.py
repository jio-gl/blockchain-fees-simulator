
from auction import AbstractAuction


class FirstPriceAuction(AbstractAuction):

    def __init__(self, max_block_size, block_time, auction_blocks):
        self.max_block_size = max_block_size
        self.block_time = block_time
        self.auction_blocks = auction_blocks
        self.partial_time = 0
        self.block_number = 0
        self.block_time_due = False

    def get_max_block_size(self):
        return self.max_block_size

    def block_price(self, block):
        return sum([ tx.gas_consumed*tx.gas_price for tx in block.block])

    def get_block_time(self):
        return self.block_time

    def sleep_wait_virtual(self, ms):
        self.partial_time += ms
        if self.partial_time > self.block_time:
            self.block_time_due = True

    def is_block_time_due(self):
        return self.block_time_due

    def execute_block(self):
        self.block_time_due = False
        self.partial_time = 0
        self.block_number += 1

    def current_block_number(self):
        return self.block_number

    def is_end_of_auction(self):
        return self.block_number >= self.auction_blocks