import sys
try:
    with open(f'{sys.argv[1]}/{sys.argv[2]}.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('fil does not exist')
    # raise err
except IOError as err:
    print('IOError')
    raise err
