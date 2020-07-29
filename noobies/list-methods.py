# basket = [1, 1, 2, 3, 4, 5]

# adding
# basket.append(100)
# insert
# basket.insert(5, 100)

# extend
# basket.extend([100, 101])


# new_list = basket
# print(basket)
# print(new_list)


# removing
# pop removed by index and return the value we popped
# basket.pop()
# basket.pop(0)

# remove , remove the value we give
# basket.pop(4) # will remove 4 from the list
# new_list = basket.pop(4)

# clear removes all the items from the array
# basket.clear()

# index will find the index of a given value. and we can give a range of index to look for
# print(basket.index(2, 0, 3))

# in return true or false of a given value.
# print('2' in basket)
# count will count the numbers of item of a given value
# print(basket.count(1))


basket = ['a', 'b', 'd', 'f', 'e', 'c', 'd']

# sort will sort the list
# basket.sort()

# sorted will return a new list
# print(sorted(basket))

new_list = basket[:]  # copying the  list

new_list = basket.copy()  # we can use copy as well

# reverse will reverse the array
basket.sort()
basket.reverse()

# print(basket[::-1])

# print(list(range(101)))

# sentence = '!'
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jojo'])
