
from random_txs import RandomTransactions
from first_price import FirstPriceAuction
from base import Block
from first_price_proposer import FirstPriceProposer

import logging, random

logging.basicConfig(level=logging.INFO)

class GasMarketSimulator:

    def __init__(self):
        self.debug = True
        self.max_block_size = 100000
        block_time = 5
        blocks_simulation=10
        self.txs_congestion_ratio = 2
        self.txs = RandomTransactions(
            skewness=4,
            average_price=100,
            block_gas_size=self.max_block_size,
            txs_per_block=50,
            block_time=5
        )
        self.auction = FirstPriceAuction(
            max_block_size=self.max_block_size,
            block_time=block_time,
            auction_blocks=blocks_simulation
        )
        self.proposer = FirstPriceProposer()

    def start_simulation(self):

        mempool = Block(max_gas_size=self.max_block_size)
        blockchain = []
        current_block = Block(max_gas_size=self.max_block_size)
        while not self.auction.is_end_of_auction():

            # 0) check block time due
            if self.auction.is_block_time_due():
                if self.debug:
                    logging.info( 'Block executed: block %d, block gas %d, total fees %d' %
                            (self.auction.current_block_number(), current_block.total_gas(),
                            self.auction.block_price(current_block)))
                self.auction.execute_block()
                blockchain.append(current_block)
                current_block = Block(max_gas_size=self.max_block_size)

            # 1) tx recv
            #for _ in range(self.txs_congestion_ratio):
            tx = self.txs.next_transaction()
            mempool.add_tx(tx)
            wait_secs = self.txs.next_wait_time_ms() #/ self.txs_congestion_ratio
            self.auction.sleep_wait_virtual(wait_secs)
            if self.debug:
                logging.info('transaction: '+str(tx))
                logging.info('new mempool size: %d' % len(mempool))
                logging.info('wait time seconds:'+str(wait_secs))

            # 2) optional, choose new tx for block
            mempool, chosen_tx = self.proposer.choose_tx_and_remove(mempool)
            logging.info('chosen tx: ' + str(chosen_tx))
            if chosen_tx and current_block.can_add_tx_size(chosen_tx):
                if chosen_tx:
                    current_block.add_tx(chosen_tx)
                if self.debug:
                    logging.info('chosen tx added to block #%d, new number of txs: %d' % (self.auction.current_block_number(),len(current_block)))
                    logging.info('block filled %.2f percent' % (100*current_block.total_gas() / self.max_block_size))
            if chosen_tx and not current_block.can_add_tx_size(chosen_tx): # going back to mempool
                mempool.add_tx(chosen_tx)


if __name__ == '__main__':

    random.seed(777)

    sim = GasMarketSimulator()
    sim.start_simulation()







