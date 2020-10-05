
from proposer import AbstractProposer


class FirstPriceProposer(AbstractProposer):

    def __init__(self):
        pass

    def choose_tx_and_remove(self, mempool):
        tx = mempool.max_gas_tx()
        mempool.remove_max_gas_tx()
        return mempool, tx

    def finish_block(self, block, mempool):
        return block