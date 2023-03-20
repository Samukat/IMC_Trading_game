class trade:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def __repr__(self) -> str:
        return f"Trade({self.volume} @ ${self.price} )"

    def is_buy(self):
        return self.price > 0
    
   
        
Trade = trade(4,2)
Yes = trade(-4,2)
print(Trade)
print(Yes)
print(Trade.is_buy())
print(Yes.is_buy())
