from itertools import groupby

string = input()

print(" ".join(["({}, {})".format(len(list(group)), char) for char, group in groupby(string)]))
