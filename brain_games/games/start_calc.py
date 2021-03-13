from random import randint, choice


RULE = 'What is the result of the expression?'


def question_and_result():
    num_one = randint(1, 99)
    num_two = randint(1, 99)
    sign = choice('-+*')
    if sign == ('-'):
        result = num_one - num_two
    elif sign == ('+'):
        result = num_one + num_two
    elif sign == ('*'):
        result = num_one * num_two
    question = str(num_one) + ' ' + sign + ' ' + str(num_two)
    return str(result), question


def main():
    question_and_result()


if __name__ == ' __main__':
    main()
