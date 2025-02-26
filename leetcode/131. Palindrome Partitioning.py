class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        res = []
        def helper(idx, curr_lst):
            if idx == len(s):
                res.append(curr_lst[:])
                return
            
            for i in range(idx, len(s)):
                if is_palindome(idx, i):
                    curr_lst.append(s[idx:i+1])
                    helper(i+1, curr_lst)
                    curr_lst.pop()
        helper(0, [])
        return res

