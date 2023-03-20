from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import numpy as np

class Trader:
    period = 15


    def __init__(self) -> None:
        self.price_log = np.zeros(Trader.period)
        self.past_day = {}


    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        print("\n\n New day/run at " + str(state.timestamp))
        print(str(state.toJSON()))
        result = {}

        for product in state.order_depths.keys():
            if (product == "BANANAS"):
                


                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []

                #average of all buy and sell orders
                average = sum(order_depth.sell_orders.keys()) + sum(order_depth.buy_orders.keys())
                denominator_for_avg = len(order_depth.sell_orders) + len(order_depth.buy_orders)
                
                #add to weighted average
                if (denominator_for_avg != 0):
                    average /= denominator_for_avg

                    if (product not in self.past_day):
                        self.past_day[product] = average

                    self.price_log = np.roll(self.price_log, 1)
                    self.price_log[0] = average - self.past_day[product] 

                    


                    # self.past_moving_avg[product] = self.moving_avg_long[product]

                    # if (self.moving_avg_short[product] == 0):
                    #     self.moving_avg_short[product] = average
                    #     self.moving_avg_long[product] = average
                    
                    # self.moving_avg_short[product] = self.moving_avg_short[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*average
                    # self.moving_avg_long[product] = self.moving_avg_long[product] * (1 - Trader.weighted_muliplier_long) + Trader.weighted_muliplier_long*average

                    # self.momentum[product] = self.momentum[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*(self.moving_avg_long[product] - self.past_moving_avg[product])
                    # print(f"Current average for {product}: " + str(average) + ", long run avg: " + str(self.moving_avg_long[product]) + ", short run avg: " + str(self.moving_avg_short[product]) + f", Momentum is {str(self.momentum[product])} ")


                print(f"MEAN IS: {self.price_log.mean()}")
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    print(f"The current best price for buying {product} is: " + str(best_ask) + ". ")

                    if self.price_log.mean() > 0: #and self.moving_avg_short[product] < self.moving_avg_long[product]:
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                if len(order_depth.buy_orders) > 0: # and ("BANANAS" in state.position) and (state.position["BANANAS"] >= 0):
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]

                    print("The current best price for selling bananas is: " + str(best_bid))

                    if self.price_log.mean() < 0:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))
            
                print(str(state.position))

            result[product] = orders

                
                

        
        return result
    
#trader = Trader()
#trader.run(example_state_1)