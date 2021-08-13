class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic1 = {}
        dic2 = {}
        bulls = 0
        cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else: 
                if secret[i] not in dic1:
                    dic1[secret[i]] = 0
                dic1[secret[i]] += 1
                if guess[i] not in dic2:
                    dic2[guess[i]] = 0
                dic2[guess[i]] += 1
        
        for c in dic1:
            if c in dic2:
                cows += min(dic1[c], dic2[c])
                
        return str(bulls) + 'A' + str(cows) + 'B'
