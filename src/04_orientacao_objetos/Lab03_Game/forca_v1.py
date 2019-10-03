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

wrongLetters = []
correctLetters = []

# Class
class Hangman:

    # Constructor
    def __init__(self, word):
        self.word = word

    # Method to guess the letter
    def guess(self, letter):
        if letter in self.word:
            correctLetters.append(letter)
            print('Possui a letra')
        else:
            wrongLetters.append(letter)
            print('Não possui uma letra na palavra')


    # Method to check if game is over
    # def hangman_over(self):

    # Method to check if the player won
    # def hangman_won(self):

    # Method to hide the letter on the board
    def hide_word(self):
        hidedWord = '*' * len(self.word)
        return hidedWord

    # Method to check the status game and print the board on the screen
    def print_game_status(self):
     print(board[0])
     print('\nWord: ' + self.hide_word())
     print('Wrong letters: ' + ', '.join(wrongLetters))
     print('Correct letters: ' + ', '.join(correctLetters))

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
    while(exit != True):
        # Check the status game
        game.print_game_status()

        # Input from user
        inputUser = input('Type a letter: ')
        game.guess(inputUser)

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
