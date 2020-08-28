my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}

print(my_dict)
