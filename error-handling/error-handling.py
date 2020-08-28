# Syntax error
# def hohoo()
#     pass


# Name error
# def hohoo():
#     1 + name
# hohoo()

# Index error
# def hohoo():
#     li = [1, 2, 3]
#     li[5]

# hohoo()


# Key Error
# def hohoo():
#     dic = {'a': 1}
#     dic['b']
# hohoo()

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter valid number')
        continue
    except ZeroDivisionError:
        print('please enter a number higher than 00')
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done4')

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'Please enter numbers {err}')


# print(sum('1', 2))
