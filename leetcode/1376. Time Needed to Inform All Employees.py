class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        team = defaultdict(list)
        for member, manager in enumerate(manager):
            team[manager].append(member)
        
        def helper(manager):
            if manager not in team:
                return 0
            
            time = 0
            for member in team[manager]:
                time = max(time, helper(member)+informTime[manager])
            
            return time
        
        return helper(headID)
