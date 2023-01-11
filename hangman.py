#!/usr/bin/env python3

from words import words
from random import choice


def hangman():
    allowed_guesses = 7

    word = choice(words).upper()
    word_guess = len(word) * '-'
    used_letters = []

    guesses = 0
    while (guesses < allowed_guesses and word_guess != word):
        print(
            f'Current word: {word_guess}\nYou have {allowed_guesses - guesses} guesses left!')

        if used_letters:
            print(
                f'You have used the following letters: {" ".join(set(used_letters))}')

        letter_guess = input("Make a guess: ").upper()
        if letter_guess in used_letters:
            print(f'You have already guessed {letter_guess}')

        elif len(letter_guess) == 1 and letter_guess.isalpha():
            used_letters.append(letter_guess)

            if letter_guess in word:
                for index, letter in enumerate(word):
                    if letter_guess == letter:
                        word_guess = word_guess[:index] + \
                            letter + word_guess[index + 1:]

            else:
                guesses += 1
        else:
            print("Please make a valid guess!")

    if word == word_guess:
        print(f'Word: {word}\nCongrats you guessed correctly!')
        return

    print(f'Word: {word}\nUnlucky, you guessed incorrectly!')
    return


def main():
    hangman()


if __name__ == "__main__":
    main()
