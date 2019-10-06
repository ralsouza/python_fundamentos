

word = 'casa'

print(list(enumerate(word)))

# idx = [i for i, value in enumerate(word) if value == 'a']

idx = [value for value, word in enumerate(word) ]

print(idx)

