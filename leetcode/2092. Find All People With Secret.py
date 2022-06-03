
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        holders = set([0, firstPerson])
        
        dic = defaultdict(list)
        for [x, y, time] in meetings:
            dic[time].append((x, y))
            
        time_lst = [(key, dic[key]) for key in dic]
        time_lst.sort(key=lambda x:x[0])
        
        def find_ancestor(parents, person):
            while person in parents and parents[person] != person:
                person = parents[person]
            return person
        
        for time, lst in time_lst:
            parents = {}
            
            for x, y in lst:
                ax = find_ancestor(parents, x)
                ay = find_ancestor(parents, y)
                
                if ax in holders and ay in holders:
                    continue
                elif ax in holders:
                    parents[ay] = ax
                    parents[ax] = ax
                else:
                    parents[ax] = ay
                    parents[ay] = ay
            
            anc_to_p = defaultdict(list)
            for p in parents:
                a = find_ancestor(parents, p)
                if a in holders:
                    anc_to_p[a].append(p)

            for a, p_lst in anc_to_p.items():
                for p in p_lst:
                    if p not in holders:
                        holders.add(p)
        
        return list(holders)
