from itertools import combinations

length_of_letters = int(input().strip())
letters = input().strip().split()
num_indices_to_select = int(input().strip())

possible_selections = list(combinations(letters, num_indices_to_select))
valid_selections = list(filter(lambda selection: any(letter == 'a' for letter in selection), possible_selections))
probability = len(valid_selections) / len(possible_selections)
print(probability)
