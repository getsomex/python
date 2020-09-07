user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 30
}
#  get method will check for a given key from dictionary and we can assign a defualt value for the key

# user2 = dict(name='john')

# print(user.get('age', 55))
# print(user2)

# print('age' in user.keys())
# print(30 in user.values())

# items will grab the item(key and value) as a tuple from dictinary
# print(user.items())

# copy will copy the dictionary
# cleat will clear the whole dictionary
# user2 = user.copy()
# user.clear()
# print(user2)

# pop in dictionary will remove the key or values from dictionary

# print(user.pop('age'))

# print(user.popitem())

# update will update a key value

user.update({'age': 55})

print(user)
