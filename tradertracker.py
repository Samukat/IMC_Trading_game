class trade:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def __repr__(self) -> str:
        return f"Trade({self.volume} @ ${self.price} )"

    def is_buy(self):
        return self.price > 0
    


class TradeTracker:
    def __init__(self):
        self.trades = []

    def add_trade(self, Trade: trade):
        self.trades.append(Trade)   

    def get_buy_trades(self, ):
        buytrades = []
        for Trade in self.trades:
            if Trade.is_buy():
                buytrades.append(Trade)
        return buytrades

    def avg(self):
        sum = 0
        for Trade in self.trades:
            sum += Trade.price  
        return sum / (len(self.trades))



tracker = TradeTracker()
tracker.add_trade(trade(7,4))
tracker.add_trade(trade(-3,4))
tracker.add_trade(trade(-1,4))
tracker.add_trade(trade(69,8))
print(tracker.get_buy_trades())
print(tracker.avg())

