# The Python code below is the minimum code that is required in a submission file:
# 1. The "datamodel" imports at the top. Using the typing library is optional.
# 2. A class called "Trader", this class name should not be changed.
# 3. A run function that takes a tradingstate as input and outputs a "result" dict.

from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
#from exmp_state import state as example_state_1

class Trader:
    weighted_muliplier_long = 0.05
    weighted_muliplier_short = 0.08

    volitility_index = {
        0:"PEARLS",
        1:"BANANAS"
    }

    stocks = ["BANANAS", "PEARLS"]


    def __init__(self) -> None:
        self.moving_avg_short = dict(zip(Trader.stocks, [0]*len(Trader.stocks)))
        self.moving_avg_long = dict(zip(Trader.stocks, [0]*len(Trader.stocks)))

        self.past_moving_avg = dict(zip(Trader.stocks, [0]*len(Trader.stocks)))
        self.momentum = dict(zip(Trader.stocks, [0]*len(Trader.stocks)))

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        print("\n\n New day/run at " + str(state.timestamp))
        result = {}

        for product in state.order_depths.keys():
            
            order_depth: OrderDepth = state.order_depths[product]
            orders: list[Order] = []

            #average of all buy and sell orders
            average = sum(order_depth.sell_orders.keys()) + sum(order_depth.buy_orders.keys())
            denominator_for_avg = len(order_depth.sell_orders) + len(order_depth.buy_orders)
            
            #add to weighted average
            if (denominator_for_avg != 0):
                average /= denominator_for_avg

                self.past_moving_avg[product] = self.moving_avg_long[product]

                if (self.moving_avg_short[product] == 0):
                    self.moving_avg_short[product] = average
                    self.moving_avg_long[product] = average
                
                self.moving_avg_short[product] = self.moving_avg_short[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*average
                self.moving_avg_long[product] = self.moving_avg_long[product] * (1 - Trader.weighted_muliplier_long) + Trader.weighted_muliplier_long*average

                self.momentum[product] = self.momentum[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*(self.moving_avg_long[product] - self.past_moving_avg[product])
                print(f"Current average for {product}: " + str(average) + ", long run avg: " + str(self.moving_avg_long[product]) + ", short run avg: " + str(self.moving_avg_short[product]) + f", Momentum is {str(self.momentum[product])} ")



            if len(order_depth.sell_orders) > 0:
                best_ask = min(order_depth.sell_orders.keys())
                best_ask_volume = order_depth.sell_orders[best_ask]
                print(f"The current best price for buying {product} is: " + str(best_ask) + ". ")

                if self.momentum[Trader.volitility_index[0]] > 0 and self.moving_avg_short[product] < self.moving_avg_long[product]:
                    print("BUY", str(-best_ask_volume) + "x", best_ask)
                    orders.append(Order(product, best_ask, -best_ask_volume))

            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                best_bid_volume = order_depth.buy_orders[best_bid]

                print("The current best price for selling bananas is: " + str(best_bid))

                if self.moving_avg_long[product] > self.moving_avg_short[product]:
                    print("SELL", str(best_bid_volume) + "x", best_bid)
                    orders.append(Order(product, best_bid, -best_bid_volume))
        


            result[product] = orders

                
                

        
        return result
    
#trader = Trader()
#trader.run(example_state_1)