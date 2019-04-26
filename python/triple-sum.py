def get_num_special_triplets(list_a, list_b, list_c):

    a_index = 0
    c_index = 0
    num_special_triplets = 0

    for b in list_b:
        while a_index < len(list_a) and list_a[a_index] <= b:
            a_index += 1

        while c_index < len(list_c) and list_c[c_index] <= b:
            c_index += 1

        num_special_triplets += a_index * c_index

    return num_special_triplets

if __name__ == '__main__':
    _ = input().split()

    # Remove duplicates and sort lists
    list_a = sorted(set(map(int, input().rstrip().split())))
    list_b = sorted(set(map(int, input().rstrip().split())))
    list_c = sorted(set(map(int, input().rstrip().split())))

    result = get_num_special_triplets(list_a, list_b, list_c)
    print(result)
