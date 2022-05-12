class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        
        def find_parent(email):
            while email in parents and email != parents[email]:
                email = parents[email]
            return email
        
        email_to_name = {}
        
        for account in accounts:
            if account[1] not in email_to_name:
                email_to_name[account[1]] = account[0]

            p = find_parent(account[1])
            parents[account[1]] = p
            for i in range(2, len(account)):
                parents[find_parent(account[i])] = p
        
        parent_to_emails = {}
        for child in parents.keys():
            p = find_parent(child)
            if p not in parent_to_emails:
                parent_to_emails[p] = []
            parent_to_emails[p].append(child)
        
        for p in parent_to_emails.keys():
            parent_to_emails[p].sort()
            parent_to_emails[p] = [email_to_name[p]] + parent_to_emails[p]
            
        return list(parent_to_emails.values())
            
            
