from functools import reduce
my_list = [1, 2, 3]

# print(list(map(lambda item: item > 1, my_list)))
print(reduce(lambda accum, item: accum+item, my_list))
