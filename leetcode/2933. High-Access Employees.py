class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        for [employee, time] in access_times:
            time = (int(time[:2]), int(time[2:]))
            dic[employee].append(time)
        
        res = []
        for employee, times in dic.items():
            times.sort()
            for i in range(2, len(times)):
                if times[i][0] == times[i-2][0] or (times[i][0] == times[i-2][0]+1 and times[i][1] < times[i-2][1]):
                    res.append(employee)
                    break
        
        return res
