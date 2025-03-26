class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        parent = {}
        def find_ancestor(node):
            if parent[node] == node:
                return node
            parent[node] = find_ancestor(parent[node])
            return parent[node]

        for [a, b] in similarPairs:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            parent[find_ancestor(b)] = find_ancestor(a)

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if word1 not in parent or word2 not in parent:
                return False
            if find_ancestor(word1) != find_ancestor(word2):
                return False

        return True
