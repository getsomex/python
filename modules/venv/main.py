# from utility import  multiply,divide
# from shopping.more_shopping.shopping_cart import buy

# print(multiply(2, 2))
#
# print(buy('apple'))

# from random import randint
# import sys
#
# answer = randint(sys.argv[1],sys.argv[2])
#
# while True:
#     try:
#         guess = int(input('guess a number:  '))
#         if 0< guess <11:
#             if guess == answer:
#                 print('You are a f**king genius 🔥')
#                 break
#         else:
#             print('Yo ! enter number between 1~10')
#     except ValueError:
#         print('Please input a number')
#         continue
#
#
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
