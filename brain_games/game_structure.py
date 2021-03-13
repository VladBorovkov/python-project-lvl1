import prompt


def start_game(start):
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(start.RULE)
    quantity_of_rounds = 3
    number_of_round = 1
    while number_of_round <= quantity_of_rounds:
        result, question, = start.question_and_result()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            number_of_round += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{result}".'
            )
            print(f"Let's try again, {name}!")
            return
        print('Congratulations, ' + name + '!')


def main():
    start_game()


if __name__ == ' __main__':
    main()
