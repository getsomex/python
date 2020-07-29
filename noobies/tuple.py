# Tuple
# tuples are like list we cannot modify them they are immutable
my_tuple = (1, 2, 3, 4, 5, 1)

# print(my_tuple[1])
# print(5 in my_tuple)
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 30,
    (1, 2): 'tuple'
}

# print(user[(1, 2)])
# tuple that has single item tends to have a comma in the end
new_tuple = my_tuple[1:3]
# print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)

# print(x)
# print(other)

# print(my_tuple.count(1))
print(my_tuple.index(10))
