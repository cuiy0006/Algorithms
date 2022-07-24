from sortedcontainers import SortedDict

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        dic = SortedDict()
        
        for i, lst in enumerate(nums):
            if lst[0] not in dic:
                dic[lst[0]] = []
            dic[lst[0]].append((i, 0))
        
        res_x = -sys.maxsize
        res_y = sys.maxsize
         
        while True:
            # print(dic)
            y, _ = dic.peekitem()
            x, tps = dic.popitem(0)
            # print(x, y)
            if y - x < res_y - res_x:
                res_y = y
                res_x = x
                
            is_continue = True
            
            for lst_idx, idx in tps:
                if idx == len(nums[lst_idx])-1:
                    is_continue = False
                    break
                num = nums[lst_idx][idx+1]
                if num not in dic:
                    dic[num] = []
                dic[num].append((lst_idx, idx+1))
            
            if not is_continue:
                break
        
        return [res_x, res_y]
