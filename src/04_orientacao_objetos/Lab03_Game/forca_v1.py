# -*- coding: utf-8 -*-

# Hangman Game https://en.wikipedia.org/wiki/Hangman_(game)
# Object-Oriented Programming

# Import
import random

# Board
board = [''' 

>>>>>>>>>>>>>>>>>> HANGMAN >>>>>>>>>>>>>>>>>>

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Class
class Hangman:

    # Constructor
    def __init__(self, word):
        self.word = word

    # Method to guess the letter
    # def guess(self, letter):

    # Method to check if game is over
    # def hangman_over(self):

    # Method to check if the player won
    # def hangman_won(self):

    # Method to hide the letter on the board
    # def hide_word(self):

    # Method to check the status game and print the board on the screen
    def print_game_status(self):
     print(board[0])

# Function to read a word randomly from the word bank
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, bank.index(max(bank)))].strip()


# Main function
def main():
    # Object
    game = Hangman(rand_word())

    # While the game is not over, print the status, request a letter and read caracter

    # Check the status game
    game.print_game_status()

    # According to the game status, print the message on screen to user
    # if game.hangman_won():
    #  print('\nCongratulations! You won!!!')
    # else:
    # print('\nGame over! You lost.')
    # print('The word was {}'.format(game.word))

    # print('\nIt was good to play with you. But now go study!\n')


# Run program
if __name__ == '__main__':
    main()
