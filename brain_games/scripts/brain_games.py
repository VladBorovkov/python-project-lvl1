#!/usr/bin/env python3

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def brain_games():
    print('Welcome to the Brain Games!')


def main():
    brain_games()
    welcome_user()


if __name__ == '__main__':
    main()
