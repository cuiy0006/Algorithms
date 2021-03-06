class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dic = {}
        for i, pp in enumerate(ppid):
            if pp in dic:
                dic[pp].append(pid[i])
            else:
                dic[pp] = [pid[i]]
            
        lst = []
        stack = [kill]
        while len(stack) != 0:
            node = stack.pop()
            lst.append(node)
            for child in dic.get(node, []):
                stack.append(child)
                
        return lst


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dic = {}
        for i, p in enumerate(ppid):
            if p not in dic:
                dic[p] = []
            dic[p].append(pid[i])
        res = []
        
        def helper(p):
            res.append(p)
            if p in dic:
                for child in dic[p]:
                    helper(child)
        
        helper(kill)
        return res
