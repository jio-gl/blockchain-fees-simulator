

class AbstractTransactions:

    def next_transaction(self):
        raise Exception('next_transaction() Not Implemented!')

    def next_wait_time_ms(self):
        raise Exception('wait_time_ms() Not Implemented!')