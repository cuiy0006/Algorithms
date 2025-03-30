class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0] * k
        res = sum(jobs)

        def dfs(idx):
            if idx == len(jobs):
                nonlocal res
                res = min(res, max(workers))
                return
            seen = set()
            for i in range(len(workers)):
                if workers[i] + jobs[idx] >= res:
                    continue
                if workers[i] in seen:
                    continue
                seen.add(workers[i])
                workers[i] += jobs[idx]
                dfs(idx+1)
                workers[i] -= jobs[idx]
        
        dfs(0)
        return res
