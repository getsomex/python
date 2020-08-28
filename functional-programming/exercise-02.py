some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dups = list(set([value for value in some_list if some_list.count(value) > 1]))

print(dups)
