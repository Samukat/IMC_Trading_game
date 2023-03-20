def should_buy(product, price, valuations):
    if product in valuations and price < valuations[product]:
        return True
    else:
        return False
    
def mystery_box_value(products, valuations):
    totalvalues = {} 
    for product in products:
        stock = products[product] * valuations[product]
        totalvalues[product] = stock
    return totalvalues




products = {'banana': 1200, 'shell' : 400, 'coconut' : 290}    
valuations = {'banana': 8, 'shell' : 4, 'coconut' : 13}
print(should_buy('banana', 7, valuations))
print(should_buy('shell', 3 , valuations))
print(should_buy('plum', 3, valuations))
print(mystery_box_value(products, valuations))

