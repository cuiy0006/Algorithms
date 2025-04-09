class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs:
            if log[:2] == '..':
                if cnt > 0:
                    cnt -= 1
            elif log[:1] == '.' and len(log) == 2:
                continue
            else:
                cnt += 1
        return cnt

