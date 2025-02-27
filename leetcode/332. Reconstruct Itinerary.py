class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        for [orig, dest] in tickets:
            if orig not in dic:
                dic[orig] = {}
            if dest not in dic[orig]:
                dic[orig][dest] = 0
            dic[orig][dest] += 1
        
        def helper(orig, curr_lst):
            if len(curr_lst) == len(tickets)+1:
                return curr_lst[:]
            if orig not in dic:
                return None
            dests = list(dic[orig])
            dests.sort()
            for dest in dests:
                dic[orig][dest] -= 1
                if dic[orig][dest] == 0:
                    del dic[orig][dest]
                curr_lst.append(dest)
                res = helper(dest, curr_lst)
                if res is not None:
                    return res
                curr_lst.pop()
                if dest not in dic[orig]:
                    dic[orig][dest] = 0
                dic[orig][dest] += 1
            return None
        
        return helper('JFK', ['JFK'])

