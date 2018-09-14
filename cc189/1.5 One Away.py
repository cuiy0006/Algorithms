def one_away(s1, s2):
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return s1[i+1:] == s2[i+1:] or s1[i+1:] == s2[i:] or s1[i:] == s2[i+1:]
    return True


inputs = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake'), ('', ' '), ('', ''), (' ', 'aa')]
outputs = [True, True, True, False, True, True, False]
for i, (s1, s2) in enumerate(inputs):
    assert one_away(s1, s2) == outputs[i]
