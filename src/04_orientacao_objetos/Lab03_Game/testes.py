
hidden = ['*','*','*','*']
word = 'casa'
letter = 'c'

print(list(enumerate(word)))

idx2 = [idx for idx, v in enumerate(word) if v == letter]

print(idx2)

print(*hidden)

for i in range(0,1):
    hidden[idx2[i]] = letter

print(*hidden)



