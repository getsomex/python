# Scope - what variables do I hace access to?

def print_func(val):
    print(val)


def sum_func():
    total = 100
    print_func(total)


sum_func()
