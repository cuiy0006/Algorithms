def is_substring(s1, s2):
    return s1 in s2


def string_rotation(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False

    for i in range(len(s1)):
        if is_substring(s1[:i], s2) and is_substring(s1[i+1:], s2):
            return True
    return False


inputs = [('waterbottle', 'erbottlewat'), ('', ''), ('abc', 'abc'), ('abc', 'bca')]
outputs = [True, False, False, True]
for i, value in enumerate(inputs):
    assert string_rotation(value[0], value[1]) == outputs[i]



