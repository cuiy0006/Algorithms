class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_cnt = 0
        task_to_cnt = defaultdict(int)
        
        for task in tasks:
            task_to_cnt[task] += 1
            max_cnt = max(max_cnt, task_to_cnt[task])
        
        num_max_cnt = 0
        for cnt in task_to_cnt.values():
            if cnt == max_cnt:
                num_max_cnt += 1
        
        if num_max_cnt >= n+1:
            return len(tasks)
        else:
            res = (n+1)*(max_cnt-1) + num_max_cnt
            if res < len(tasks):
                return len(tasks)
            else:
                return res
