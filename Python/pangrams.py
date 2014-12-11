test_string = raw_input()
test_arr = []

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
test_arr.extend(test_string.lower())

for i in range(len(test_arr)):
    if alphabet.count(test_arr[i]) != 0:
        alphabet.remove(test_arr[i])

if alphabet == []:
    print "pangram"
else:
    print "not pangram"