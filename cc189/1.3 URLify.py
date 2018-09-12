def URLify(str_arr):
    i = len(str_arr) - 1
    j = i
    while j >= 0 and str_arr[j] == ' ':
        j -= 1

    if j != len(str_arr) - 1:
        while j >= 0:
            str_arr[i] = str_arr[j]
            str_arr[j] = ' '
            i -= 1
            j -= 1

    j = 0
    while j < len(str_arr) and str_arr[j] == ' ':
        j += 1
    i = 0

    while j < len(str_arr):
        if str_arr[j] != ' ':
            str_arr[i] = str_arr[j]
            i += 1
            j += 1
        else:
            str_arr[i], str_arr[i+1], str_arr[i+2] = '%', '2', '0'
            i += 3
            while str_arr[j] == ' ':
                j += 1
    while i < len(str_arr):
        str_arr[i] = ' '
        i += 1


str_lst = ['', '   ', '  hello world  ', '    abb cvv', 'asd ']
res_lst = [[], [' ', ' ', ' '], ['h', 'e', 'l', 'l', 'o', '%', '2', '0', 'w', 'o', 'r', 'l', 'd', ' ', ' '], ['a', 'b', 'b', '%', '2', '0', 'c', 'v', 'v', ' ', ' '], ['a', 's', 'd', ' ']]
for i, s in enumerate(str_lst):
    str_arr = list(s)
    URLify(str_arr)
    assert str_arr == res_lst[i]


