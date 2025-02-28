class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def helper(idx, left, curr_lst):
            if idx == len(s) and left == 0:
                res.append('.'.join(curr_lst))
                return
            elif idx > len(s)-1 or left == 0:
                return

            for i in range(idx, idx+3):
                if s[idx] == '0' and i != idx:
                    continue
                curr = s[idx:i+1]
                if int(curr) > 255:
                    continue
                curr_lst.append(curr)
                helper(i+1, left-1, curr_lst)
                curr_lst.pop()
        helper(0, 4, [])
        return res

