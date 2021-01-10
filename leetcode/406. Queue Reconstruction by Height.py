class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda one: (one[0], -one[1]))
        
        res = [None for one in people]
        indexes = [i for i in range(len(people))]
        
        for one in people:
            idx = indexes.pop(one[1])
            res[idx] = one
        return res
        
        
        
        
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = [[one[0], one[1], one[1]] for one in people]
        people.sort(key=lambda one: (one[0], -one[1]))
        
        res = []
        while len(res) < len(people):
            for i in range(len(people)):
                if people[i] == None:
                    continue
                if people[i][2] == 0:
                    res.append([people[i][0], people[i][1]])
                    people[i] = None
                    break
                else:
                    people[i][2] -= 1

        return res
