def string_compression(s):
    i = 0
    curr = None
    curr_cnt = 0
    res = []

    while i < len(s):
        if curr is None:
            curr = s[i]
            curr_cnt = 1
        else:
            if curr == s[i]:
                curr_cnt += 1
            else:
                res.append(curr)
                res.append(str(curr_cnt))
                curr = s[i]
                curr_cnt = 1
        i += 1
    if curr is not None:
        res.append(curr)
        res.append(str(curr_cnt))
    res = ''.join(res)
    return res if len(res) < len(s) else s


inputs = ['', 'aaabbbcc', 'abccvva', 'aaaaa']
outputs = ['', 'a3b3c2', 'abccvva', 'a5']
for i, value in enumerate(inputs):
    assert outputs[i] == string_compression(value)
