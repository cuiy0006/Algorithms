def check_permutation_1(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))

def check_permutation_2(s1, s2):
    if len(s1) != len(s2):
        return False
    dic = {}
    for c in s1:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    for c in s2:
        if c in dic and dic[c] > 0:
            dic[c] -= 1
        else:
            return False

    return True


true_lst = [('asdswea', 'sasadwe'), ('', ''), ('123454321', '321321445')]
false_lst = [('aaaa', 'aaa'), ('qweqe', 'ewqe'), ('zxczx', 'gfhfgh'), ('', 'asdqe'), ('xcxzc', '')]

for s1, s2 in true_lst:
    assert check_permutation_1(s1, s2)
    assert check_permutation_2(s1, s2)

for s1, s2 in false_lst:
    assert not check_permutation_1(s1, s2)
    assert not check_permutation_2(s1, s2)



