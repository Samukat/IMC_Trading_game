from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import numpy as np
#from Example_data.json_state_importer import import_state

class Trader:
    period = 1000


    def __init__(self) -> None:
        self.past_days_value = {}
        self.past_days_timestamp = {}


    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        print("\n\n New day/run at " + str(state.timestamp))
        print(str(state.toJSON()))
        result = {}

        for product in state.order_depths.keys():
            if (product == True):
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []

                #average of all buy and sell orders
                total_price = sum(trade.price*trade.quantity for trade in state.market_trades[product])
                quantity = sum(trade.quantity for trade in state.market_trades[product])
                
                #add to weighted average
                if (quantity != 0):
                    average = total_price / quantity



                    if (product not in self.past_days_value):
                        self.past_days_value[product] = np.zeros(Trader.period)
                        self.past_days_timestamp[product] = np.zeros(Trader.period)

                    self.past_days_value[product] = np.roll(self.past_days_value[product], 1)
                    self.past_days_value[product][0] = average

                    self.past_days_timestamp[product] = np.roll(self.past_days_timestamp[product], 1)
                    self.past_days_timestamp[product][0] = state.timestamp
                    
                    

                    polynomial = np.poly1d(np.polyfit(self.past_days_timestamp[product],self.past_days_value[product],4))
                    print(f"AAAA: {str(self.past_days_value[product])}, BBB: {polynomial}")
                    
                    


                    # self.past_moving_avg[product] = self.moving_avg_long[product]

                    # if (self.moving_avg_short[product] == 0):
                    #     self.moving_avg_short[product] = average
                    #     self.moving_avg_long[product] = average
                    
                    # self.moving_avg_short[product] = self.moving_avg_short[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*average
                    # self.moving_avg_long[product] = self.moving_avg_long[product] * (1 - Trader.weighted_muliplier_long) + Trader.weighted_muliplier_long*average

                    # self.momentum[product] = self.momentum[product] * (1 - Trader.weighted_muliplier_short) + Trader.weighted_muliplier_short*(self.moving_avg_long[product] - self.past_moving_avg[product])
                    # print(f"Current average for {product}: " + str(average) + ", long run avg: " + str(self.moving_avg_long[product]) + ", short run avg: " + str(self.moving_avg_short[product]) + f", Momentum is {str(self.momentum[product])} ")


                print(f"MEAN IS: {self.past_days_value[product].mean()}")
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    print(f"The current best price for buying {product} is: " + str(best_ask) + ". ")

                    if (best_ask < polynomial(state.timestamp+100)): #and self.moving_avg_short[product] < self.moving_avg_long[product]:
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                if len(order_depth.buy_orders) > 0: # and ("BANANAS" in state.position) and (state.position["BANANAS"] >= 0):
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]

                    print("The current best price for selling bananas is: " + str(best_bid))

                    if (best_bid > polynomial(state.timestamp+100)):
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))
            
                print(str(state.position))

                result[product] = orders

        
                
                

        
        return result
    
#trader = Trader()
#trader.run(import_state("example_data.json"))