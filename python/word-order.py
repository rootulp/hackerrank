from collections import OrderedDict

num_words = int(input().strip())
word_occurences = OrderedDict()
for _ in range(num_words):
    word = input().strip()
    if(word in word_occurences):
        word_occurences[word] += 1
    else:
        word_occurences[word] = 1

print(len(word_occurences))
print(" ".join(map(str, word_occurences.values())))
