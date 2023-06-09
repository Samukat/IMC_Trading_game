from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order


class Trader:
    def __init__(self):
        self.past_day = 0
        self.dayslist = []
        self.sum = 0
        self.current_day = 0
        self.gradient = 0
        self.sell = 0
        self.buy = 0

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        result = {}

        # Iterate over all the keys (the available products) contained in the order dephts
        for product in state.order_depths.keys():
            print(product)


            # Check if the current product is the 'PEARLS' product, only then run the order logic
            if product == 'PEARLS':
                # Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
                order_depth: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders: list[Order] = []


                # Define a fair value for the PEARLS.
                # Note that this value o 1 is just a dummy value, you should likely change it!

                print(order_depth.sell_orders)
                self.current_day = sum(trade.price*trade.quantity for trade in state.market_trades[product])/sum(trade.quantity for trade in state.market_trades[product])
                if sum > 5:
                    self.gradient = (self.current_day - self.dayslist[sum])/5
                    if self.gradient >= 5:
                        self.sell = 1
                        self.buy = 0
                    elif self.gradient > -5:
                        self.buy = 0
                        self.sell = 0
                    elif self.gradient <= -5:
                        self.buy = 1
                        self.sell = 0
                        


                # If statement checks if there are any SELL orders in the PEARLS market
                if len(order_depth.sell_orders) > 0:

                    

                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    



                    # Check if the lowest ask (sell order) is lower than the above defined fair value
                    if self.buy == 1:

                        # In case the lowest ask is lower than our fair value,
                        # This presents an opportunity for us to buy cheaply
                        # The code below therefore sends a BUY order at the price level of the ask,
                        # with the same quantity
                        # We expect this order to trade with the sell order
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                # The below code block is similar to the one above,
                # the difference is that it find the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if self.sell == 1:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))


                # Add all the above the orders to the result dict
                result[product] = orders

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above

                self.past_day = sum(trade.price*trade.quantity for trade in state.market_trades[product])/sum(trade.quantity for trade in state.market_trades[product])
                self.dayslist.append(self.past_day)
                sum += 1
                

        return result
    

