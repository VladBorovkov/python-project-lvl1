from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(question):
    if question <= 1:
        return False
    else:
        counter = 2
        while counter <= question / 2:
            if question % counter == 0:
                return False
            counter += 1
        return True


def question_and_result():
    question = randint(1, 99)
    if prime(question):
        result = 'yes'
    else:
        result = 'no'
    return result, str(question)


def main():
    question_and_result()


if __name__ == ' __main__':
    main()

