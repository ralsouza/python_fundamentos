
hidedWord = []
word = 'Teste'
letter = 'e'

def hide_word():
    hidedWord = ['*' for x in word]
    return hidedWord

hidedWord = hide_word()

print('Word: ' + ''.join(hidedWord))

hidedWord[2] = 'b'
hidedWord[3] = 'c'

print('Word: ' + ''.join(hidedWord))


# if letter in word:
#     print()
