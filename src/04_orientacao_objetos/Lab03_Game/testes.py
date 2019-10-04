
hidedWord = []
word = 'Teste'
letter = 'e'

def hide_word(word):
    hidedWord.append('*' * len(word))
    return hidedWord

hide_word(word)

print('Word: ' + ''.join(hidedWord))

hidedWord[2]




# if letter in word:
#     print()