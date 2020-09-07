# Set
# unordered collections of unique objects
# set doesn't support indexing
my_set = {4, 5, }
your_set = {4, 5, 6, 7, 8}
# add
# add will add item to the set however we can not add any duplicate
# my_set.add(100)
# my_set.add(2)


my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))

# print(1 in my_set)

# print(len(my_set))

# changing set to list
# print(list(my_set))

# copy

my_set2 = my_set.copy()

# my_set.clear()
# print(my_set)
# print(my_set2)

# difference
# difference copmare between two sets and return the values that are not in the other set
# wont modify the set
# print(my_set.difference(your_set))

# discard
# discard will take out the given value from the set
# my_set.discard(5)
# difference_update modify the set
# print(my_set.difference_update(your_set))


# intersection
# intersection will get the common things between two sets
# print(my_set.intersection(your_set))

# isdisjoint
# isdisjoint means sets have nothing common
# print(my_set.isdisjoint(your_set))

# union
# print(my_set.union(your_set))
# print(my_set | your_set)

# subset
print(my_set.issubset(your_set))

# superset
print(my_set.issuperset(your_set))
