def anagram(str):
    if len(str) % 2 == 1:
        return "-1"
    else:
        str_arr = []
        str_arr.extend(str)
        a = str_arr[:len(str_arr)/2]
        b = str_arr[(len(str_arr)/2):]

        count = 0
        for index in range(len(a)):
            if b.count(a[index]) != 0:
                b.remove(a[index])
            else:
                count += 1

        return count


test_cases = int(raw_input())
for x in range(test_cases):
    str = raw_input()
    print(anagram(str))
