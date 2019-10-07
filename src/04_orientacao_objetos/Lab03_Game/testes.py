
hidden = ['*','*','*','*']
word = 'casa'
letter = 'a'

print(list(enumerate(word)))

idx2 = [idx for idx, v in enumerate(word) if v == letter]

print(idx2)

print(*hidden)

for i in range(0,len(word)):
    if (i == idx2[i]):
        print(i)



