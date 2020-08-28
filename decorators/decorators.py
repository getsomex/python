def my_decorator(func):
    def wrap_func(greeting):
        print('****')
        func(greeting)
        print('****')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('hello')
