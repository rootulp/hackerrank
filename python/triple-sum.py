

# A special triplet is defined as: a <= b <= c for
# a in list_a, b in list_b, and c in list_c
def get_num_special_triplets(list_a, list_b, list_c):
    # remove duplicates and sort lists
    list_a = sorted(set(list_a))
    list_b = sorted(set(list_b))
    list_c = sorted(set(list_c))

    num_special_triplets = 0

    for b in list_b:
        len_a_candidates = num_elements_less_than(b, list_a)
        len_c_candidates = num_elements_less_than(b, list_c)
        num_special_triplets += 1 * len_a_candidates * len_c_candidates

    return num_special_triplets


def num_elements_less_than(target, sorted_list):
    for index, candidate in enumerate(sorted_list):
        if candidate > target:
            return index
    return len(sorted_list)

if __name__ == '__main__':
    _ = input().split()
    list_a = list(map(int, input().rstrip().split()))
    list_b = list(map(int, input().rstrip().split()))
    list_c = list(map(int, input().rstrip().split()))
    num_special_triplets = get_num_special_triplets(list_a, list_b, list_c)
    print(num_special_triplets)
