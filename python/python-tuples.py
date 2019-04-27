if __name__ == '__main__':
    num_integers = int(input())
    integers = tuple(map(int, input().split()))
    print(hash(integers))
