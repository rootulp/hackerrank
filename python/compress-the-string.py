from itertools import groupby

string = input()
groups = [(len(list(group)), int(char)) for char, group in groupby(string)]
print(" ".join([str(tup) for tup in groups]))
