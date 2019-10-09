
hidden = ['*','*','*','*']
word = 'casa'
letter = 'a'

print(list(enumerate(word)))

idx2 = [idx for idx, v in enumerate(word) if v == letter]

print(idx2)

print(*hidden)

for i in range(len(idx2)):
    hidden[idx2[i]] = letter

print(*hidden)

print(word[0])



