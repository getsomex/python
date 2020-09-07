import sys
from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open(f'{sys.argv[1]}/{sys.argv[2]}.txt', mode='r') as my_file:
        trnaslation = translator.translate(my_file.read())
        print(trnaslation)
except FileNotFoundError as err:
    print('file not found')
