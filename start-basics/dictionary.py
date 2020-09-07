# Dictionary
#  a dictionary is an unordered key value pair
# unordered means they are not next to each other in　memory
# since dictionary is unordered we can not grab them by index unlike list
dictionary = {
    'a': 1,
    'b': 'hello',
    'c': [1, 2, 3, 4],
    'd': True

}
my_list = [
    {
        'a': 1,
        'b': 'hello',
        'c': [1, 2, 3, 4],
        'd': True
    },
    10
]
print(my_list[0]['c'][2])
