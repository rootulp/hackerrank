

# A special triplet is defined as: a <= b <= c for
# a in list_a, b in list_b, and c in list_c
def get_num_special_triplets(list_a, list_b, list_c):
    special_triplets = set()
    for a in list_a:
        for b in list_b:
            for c in list_c:
                if a <= b >= c:
                    special_triplets.add((a, b, c))
    return len(special_triplets)

if __name__ == '__main__':
    _ = input().split()
    list_a = list(map(int, input().rstrip().split()))
    list_b = list(map(int, input().rstrip().split()))
    list_c = list(map(int, input().rstrip().split()))
    num_special_triplets = get_num_special_triplets(list_a, list_b, list_c)
    print(num_special_triplets)
