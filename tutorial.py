# The Python code below is the minimum code that is required in a submission file:
# 1. The "datamodel" imports at the top. Using the typing library is optional.
# 2. A class called "Trader", this class name should not be changed.
# 3. A run function that takes a tradingstate as input and outputs a "result" dict.

from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
from exmp_state import state as example_state_1

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
		Takes all buy and sell orders for all symbols as an input,
		and outputs a list of orders to be sent
		"""
        for listing in state.listings.keys():
            print(listing)

        result = {}
        return result
    
trader = Trader()
trader.run(example_state_1)