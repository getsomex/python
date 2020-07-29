def highest_even(li):
    li.sort()
    maxEven = []
    for item in li:
        if(item % 2 == 0):
            maxEven.append(item)

    return maxEven[(len(maxEven)-1)]


print(highest_even([10, 2, 1, 4, 3, 20]))
