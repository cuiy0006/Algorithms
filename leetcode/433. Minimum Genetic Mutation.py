class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if startGene not in bank:
            bank.add(startGene)
        if endGene not in bank:
            return -1
        q = deque([startGene])
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                gene = q.popleft()
                if gene == endGene:
                    return d
                if gene not in bank:
                    continue
                bank.remove(gene)
                for c in ('A', 'C', 'G', 'T'):
                    for i in range(len(gene)):
                        q.append(gene[:i] + c + gene[i+1:])
            d += 1
        
        return -1

