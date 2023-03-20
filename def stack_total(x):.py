def stack_total(x):
    sum = 0
    while x != 0:
        sum = sum + x
        x = x -1
    return sum

x = 6
print(stack_total(x))