from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a f**king genius 🔥')
            return True
    else:
        print('Yo ! enter number between 1~10')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number:  '))
            if(run_guess(guess, answer)):
                break

        except ValueError:
            print('Please input a number')
            continue
