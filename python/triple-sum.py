

# A special triplet is defined as: a <= b <= c for
# a in list_a, b in list_b, and c in list_c
def get_num_special_triplets(list_a, list_b, list_c):
    num_special_triplets = 0

    for b in list_b:
        len_a_candidates = len([a for a in list_a if a <= b])
        len_c_candidates = len([c for c in list_c if c <= b])
        num_special_triplets += 1 * len_a_candidates * len_c_candidates

    return num_special_triplets

if __name__ == '__main__':
    _ = input().split()
    list_a = list(set(map(int, input().rstrip().split())))
    list_b = list(set(map(int, input().rstrip().split())))
    list_c = list(set(map(int, input().rstrip().split())))
    num_special_triplets = get_num_special_triplets(list_a, list_b, list_c)
    print(num_special_triplets)
