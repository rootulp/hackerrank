if __name__ == '__main__':
    string = input()
    print(any(filter(str.isalnum, string)))
    print(any(filter(str.isalpha, string)))
    print(any(filter(str.isdigit, string)))
    print(any(filter(str.islower, string)))
    print(any(filter(str.isupper, string)))
