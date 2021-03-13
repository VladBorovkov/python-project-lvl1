from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def question_and_result():
    num_one = randint(1, 99)
    num_two = randint(1, 99)
    question = str(num_one) + ' ' + str(num_two)
    while num_one != 0 and num_two != 0:
        if num_one > num_two:
            num_one %= num_two
        else:
            num_two %= num_one
    result = num_one + num_two
    return str(result), question


def main():
    question_and_result()


if __name__ == ' __main__':
    main()
