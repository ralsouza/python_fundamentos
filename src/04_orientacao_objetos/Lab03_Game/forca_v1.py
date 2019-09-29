# -*- coding: utf-8 -*-

# Hangman Game https://en.wikipedia.org/wiki/Hangman_(game)
# Object-Oriented Programming

# Import
import random

# Board
board = [ ''' 

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
=========''' ]

# Class
class Hangman:

    # Contructor
    def __init__(self, word):

    # Method to guess the letter
    def guess(self, letter):

    # Method to check if game is over
    def hangman_over(self):

    # Method to check if the player won
    def hangman_won(self):

    # Method to hide the letter on the board
    def hide_word(self):

    # Method to check the status game and print the board on the screen
    def print_game_status(self):

# Function to read a word randomly from the word bank
def rand_word():
    with open('palavras.txt','rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Main function
def main():
    # Object
    game = Hangman(rand_word())

