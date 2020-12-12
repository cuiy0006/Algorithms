class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emailToName = {}
        parent ={}
        parentToSet = {}
        def findParent(email):
            while email != parent[email]:
                email = parent[email]
            return email
        for account in accounts:
            emailToName[account[1]] = account[0]
            for i in range(1, len(account)):
                parent[account[i]] = account[i]
        for account in accounts:
            p = findParent(account[1])
            for i in range(2, len(account)):
                parent[findParent(account[i])] = p
        for account in accounts:
            p = findParent(account[1])
            if p not in parentToSet:
                parentToSet[p] = set()
            for i in range(1, len(account)):
                parentToSet[p].add(account[i])
        res = []
        for p in parentToSet:
            account = [emailToName[p]]
            account += sorted(list(parentToSet[p]))
            res.append(account)
        return res
                
