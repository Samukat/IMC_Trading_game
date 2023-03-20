# The Python code below is the minimum code that is required in a submission file:
# 1. The "datamodel" imports at the top. Using the typing library is optional.
# 2. A class called "Trader", this class name should not be changed.
# 3. A run function that takes a tradingstate as input and outputs a "result" dict.

from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
#from exmp_state import state as example_state_1

class Trader:
    weighted_muliplier_long = 0.01
    weighted_muliplier_short = 0.03


    def __init__(self) -> None:
        self.intialised = False
        self.moving_avg_short = 0  #assume -1 is not initalised
        self.moving_avg_long = 0

        self.past_moving_avg_long = 0 

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
		Takes all buy and sell orders for all symbols as an input,
		and outputs a list of orders to be sent
		"""
        print("\n\n New day/run at " + str(state.timestamp))



        result = {}

        for product in state.order_depths.keys():
            if True: #product == "BANANAS": #this was stupid as there aint muliple averages

                
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []

                #average of all buy and sell orders
                average = sum(order_depth.sell_orders.keys()) + sum(order_depth.buy_orders.keys())
                denominator_for_avg = len(order_depth.sell_orders) + len(order_depth.buy_orders)
                
                #add to weighted average
                if (denominator_for_avg != 0):
                    average /= denominator_for_avg

                    self.past_moving_avg_long = self.moving_avg_long

                    #if (self.moving_avg_short == 0):
                    #    self.moving_avg_short = average
                     #   self.moving_avg_long = average
                    
                    self.moving_avg_short = self.moving_avg_short * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*average
                    self.moving_avg_long = self.moving_avg_long * (1 - Trader.weighted_muliplier_long) + Trader.weighted_muliplier_long*average

                    print("Current average: " + str(average) + ", long run avg: " + str(self.moving_avg_long) + ", short run avg: " + str(self.moving_avg_short) + ". ")



                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    print("The current best price for buying bananas is: " + str(best_ask) + ". ")

                    if self.moving_avg_short < self.moving_avg_long and self.past_moving_avg_long < self.moving_avg_long:
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                if len(order_depth.buy_orders) > 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]

                    print("The current best price for selling bananas is: " + str(best_bid))

                    if self.moving_avg_short > self.moving_avg_long:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))
            


            result[product] = orders

                
                

        
        return result
    
#trader = Trader()
#trader.run(example_state_1)