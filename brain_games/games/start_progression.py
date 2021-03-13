from random import randint


RULE = 'What number is missing in the progression?'


def question_and_result():
    progression_size = 10
    start_num = randint(1, 99)
    position_excluded_num = randint(0, progression_size - 1)
    step = randint(1, 100)
    index_num = 0
    question = ''
    while index_num < progression_size:
        if index_num == position_excluded_num:
            question += '.. '
            index_num += 1
        else:
            question += f'{start_num + step * index_num} '
            index_num += 1
    result = start_num + step * position_excluded_num
    return str(result), question.rstrip()


def main():
    question_and_result()


if __name__ == ' __main__':
    main()
