
class AbstractAuction:

    def get_max_block_size(self):
        raise Exception('max_block_size() Not Implemented!')

    def block_price(self, block):
        raise Exception('block_price() Not Implemented!')

    def get_block_time(self):
        raise Exception('block_time() Not Implemented!')

    def sleep_wait_virtual(self, ms):
        raise Exception('sleep_wait_virtual() Not Implemented!')

    def current_block_number(self):
        raise Exception('sleep_wait_virtual() Not Implemented!')

    def is_end_of_auction(self):
        raise Exception('sleep_is_end_of_auctionwait_virtual() Not Implemented!')