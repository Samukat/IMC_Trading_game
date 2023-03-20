
def crate_bananas(bunches):
    i = 0
    crates = []
    while (i < len(bunches)):
        crates.append(min(bunches[i], 20))
        i += 1
    return crates
print(crate_bananas([10,15,20,23,24,12,25]))
