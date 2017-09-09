from collections import Counter


def ransom_note(magazine_words, ransom_words):
    available_words = Counter(magazine_words)
    needed_words = Counter(ransom_words)
    return contains(available_words, needed_words)


def contains(larger, smaller):
    return not smaller - larger

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
