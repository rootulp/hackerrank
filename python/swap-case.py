def swap_case(string):
    """
    Convert all lowercase letters to upercase letters and vice versa.
    """
    return string.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
