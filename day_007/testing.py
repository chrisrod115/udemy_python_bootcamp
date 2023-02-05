store_indexes = []

guess_let = "l"
rand_word = "hello"
for i in range(len(rand_word)):
    while guess_let == rand_word[i]:
        store_indexes = i

print(store_indexes)
