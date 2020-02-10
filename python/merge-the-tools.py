from collections import OrderedDict

def merge_the_tools(string, split_length):
    splits = split_strings(string, split_length)
    result = remove_repeats(splits)
    print ("\n".join(result))


def split_strings(string, split_length):
    return [string[i : i + split_length] for i in range(0, len(string), split_length)]


def remove_repeats(strings):
    return ["".join(OrderedDict.fromkeys(string)) for string in strings]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
