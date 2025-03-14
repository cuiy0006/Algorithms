class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        lst = preorder.split(',')
        def checkbuild(idx):
            if idx > len(lst)-1:
                return False, None
            if lst[idx] == '#':
                return True, idx+1
            idx += 1
            legal, idx = checkbuild(idx)
            if not legal:
                return False, None
            legal, idx = checkbuild(idx)
            if not legal:
                return False, None
            return True, idx

        legal, idx = checkbuild(0)
        if not legal:
            return False
        if idx != len(lst):
            return False
        return True
