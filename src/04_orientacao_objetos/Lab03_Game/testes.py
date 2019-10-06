

word = 'casa'

print(list(enumerate(word)))

idx2 = [idx for idx, v in enumerate(word) if v == 'a']

print(idx2)

