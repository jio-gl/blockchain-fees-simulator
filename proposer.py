

class AbstractProposer:

    def choose_tx(self, mempool):
        raise Exception('choose_tx() Not Implemented!')

    def get_current_block(self):
        raise Exception('get_current_block() Not Implemented!')

    def finish_block(self):
        raise Exception('finish_block() Not Implemented')