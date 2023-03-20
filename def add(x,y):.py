def classify_price(x, y = 8, z = 12):
    if x < y:
        print("good")
    elif x > z:
        print("bad")
    else:
        print("ok")
    
def test(x):
    if x == 4:
        return 'real bad'
    else:
        classify_price(x)

print(test(5))