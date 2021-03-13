from random import randint


RULE = 'Answer "yes" if number even otherwise answer "no".'


def question_and_result():
    question = randint(1, 99)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, str(question)


def main():
    question_and_result()


if __name__ == ' __main__':
    main()
