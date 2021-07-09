class Solution:
    def modifyString(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lst = list(s)
        
        for i, c in enumerate(lst):
            if c == '?':
                for letter in letters:
                    if i == 0 and i == len(lst) - 1:
                        lst[i] = letter
                    elif i == 0:
                        if letter != lst[i + 1]:
                            lst[i] = letter
                            break
                    elif i == len(lst) - 1:
                        if letter != lst[i - 1]:
                            lst[i] = letter
                            break
                    else:
                        if letter != lst[i + 1] and letter != lst[i - 1]:
                            lst[i] = letter
                            break
                            
        return ''.join(lst)
                    
