def is_unique_1(s):
    char_set = set()
    for c in s:
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True


def is_unique_2(s):
    flag = 0
    for c in s:
        bit_index = ord(c) - ord('a')
        if flag & (1 << bit_index) >= 1:
            return False
        else:
            flag = flag | (1 << bit_index)
    return True


def is_unique_3(s):
    return not any(s[i] == s[j] for i in range(len(s)) for j in range(i+1, len(s)))
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)):
    #         if s[i] == s[j]:
    #             return False
    # return True


def is_unique_4(s):
    lst = list(s)
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            return False
    return True


s_true_lst = ['123456', '1a2b3c4d', '', 'a']
s_false_lst = ['a11123', 'x12qe4x', 'aa']

s_aphabetic_true_lst = ['asdfqwex', 'qwexc', '', 'a']
s_aphabetic_false_lst = ['asqwgffg', 'qq', 'qaqaq']

for s in s_true_lst:
    assert is_unique_1(s)
    assert is_unique_3(s)
    assert is_unique_4(s)

for s in s_false_lst:
    assert not is_unique_1(s)
    assert not is_unique_3(s)
    assert not is_unique_4(s)

for s in s_aphabetic_true_lst:
    assert is_unique_2(s)

for s in s_aphabetic_false_lst:
    assert not is_unique_2(s)

