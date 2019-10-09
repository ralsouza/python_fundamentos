# -*- coding: utf-8 -*-

# Hangman Game https://en.wikipedia.org/wiki/Hangman_(game)
# Object-Oriented Programming

# Import
import random
import sys
# Board
board = [''' 

>>>>>>>>>>>>>>>>>> HANGMAN >>>>>>>>>>>>>>>>>>
https://en.wikipedia.org/wiki/Hangman_(game)

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

# Create lists to store data
wrongLetters = []
correctLetters = []
hiddenWord = []

# Class
class Hangman:

    # Constructor
    def __init__(self, word):
        self.word = word
        self.hiddenWord = self.hide_word()

    # Method to guess the letter
    def guess(self, letter):
        if letter in self.word:
            # Append guessed letter into correct letters list
            correctLetters.append(letter)

            if (len(correctLetters) == len(self.word)):
                self.hangman_won()

            # Extract the index or indexes of position/s guessed letter
            idx = [idx for idx, v in enumerate(self.word) if v == letter]

            # Replace guessed letter into the correspondent position in the hidden word
            for i in range(len(idx)):
                self.hiddenWord[idx[i]] = letter
                print(self.word)
        else:
            wrongLetters.append(letter)

            # Check if gamer lost
            if(len(wrongLetters) == len(self.word)):
                self.hangman_over()

    # Method to check if game is over
    def hangman_over(self):
        sys.exit('\nGAME OVER! \nThe word was: {} \nTry again.'.format(self.word))

    # Method to check if the player won
    def hangman_won(self):
        sys.exit('\nYOU WON! \nNow, go to study!!!')

    # Method to hide the letter on the board
    def hide_word(self):
        return ['*' for x in self.word]

    # Method to check the status game and print the board on the screen
    def print_game_status(self):
     # Draws the hangman on the board
     print(board[len(wrongLetters)])

     # Print the hidden word on the board
     print(*self.hiddenWord)

     # Print the wrong letters on the board
     print('Wrong letters: ' + ', '.join(wrongLetters))

     # Print the correct letters on the board
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

# Run program
if __name__ == '__main__':
    main()