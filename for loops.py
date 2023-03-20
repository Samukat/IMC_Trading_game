def count_bananas(crates):
    sum = 0
    most = 0
    for crate in crates:
        for banana in crate:
            most = max(most, banana)
            sum += banana

    return sum, most

print(count_bananas([[25,100,25], [40,35,20], [90,5]]))