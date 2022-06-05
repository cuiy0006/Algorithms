class Solution:
    def minJumps(self, arr: List[int]) -> int:
        seen = set()
        
        q = deque([0])
        
        dic = defaultdict(list)
        
        for i, word in enumerate(arr):
            dic[word].append(i)
        
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                idx = q.popleft()

                if idx == len(arr)-1:
                    return d
                if idx > 0:
                    if idx-1 not in seen:
                        seen.add(idx-1)
                        q.append(idx-1)
                        
                if idx+1 not in seen:
                    seen.add(idx+1)
                    q.append(idx+1)

                for i in dic[arr[idx]]:
                    if i not in seen:
                        seen.add(i)
                        q.append(i)
                dic[arr[idx]].clear()
            d += 1
            
        return -1
