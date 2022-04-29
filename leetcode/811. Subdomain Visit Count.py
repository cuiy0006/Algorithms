class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_to_cnt = defaultdict(int)
        
        for cpdomain in cpdomains:
            [cnt, domain] = cpdomain.split(' ')
            
            lst = domain.split('.')
            
            curr = lst[-1]
            i = len(lst) - 2
            while i >= 0:
                domain_to_cnt[curr] += int(cnt)
                curr = lst[i] + '.' + curr
                i -= 1

            domain_to_cnt[curr] += int(cnt)
            
        return [str(cnt) + ' ' + domain for domain, cnt in domain_to_cnt.items()]
            
