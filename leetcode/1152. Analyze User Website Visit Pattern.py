class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        zipped = list(zip(username, website, timestamp))
        zipped.sort(key=lambda x:x[2])
        
        user_to_words = defaultdict(list)
        for i in range(len(zipped)):
            user_to_words[zipped[i][0]].append(zipped[i][1])

        user_to_patterns = defaultdict(set)
        
        for user, words in user_to_words.items():
            for i in range(len(words)):
                for j in range(i+1, len(words)):
                    for k in range(j+1, len(words)):
                        user_to_patterns[user].add((words[i], words[j], words[k]))
        
        pattern_to_cnt = defaultdict(int)
        for patterns in user_to_patterns.values():
            for pattern in patterns:
                pattern_to_cnt[pattern] += 1
        

        max_cnt = max(pattern_to_cnt.values())
        res = [pattern for pattern, cnt in pattern_to_cnt.items() if cnt == max_cnt]
        res.sort()
        return res[0]
