def palindrome_permutation(s):
    char_set = set()
    for c in s:
        if c == ' ':
            continue
        c = c.lower()
        if c in char_set:
            char_set.remove(c)
        else:
            char_set.add(c)
    return len(char_set) == 1 or len(char_set) == 0


inputs = ['', ' ', 'Tact Coa', ' qwe a ewq aa sdd ' ' as da sd qq qx c']
outputs = [True, True, True, False, False]

for i, s in enumerate(inputs):
    assert palindrome_permutation(s) == outputs[i]

