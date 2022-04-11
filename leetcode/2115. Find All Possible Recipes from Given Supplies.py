from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r_to_i = {
            recipes[i]: set(ingredients[i]) for i in range(len(recipes)) 
        }
        
        res = []
        
        q = deque(supplies)
        
        while len(q) != 0:
            supply = q.popleft()
            lst = list(r_to_i.items())
            
            for recipe, in_set in lst:
                if supply in in_set:
                    in_set.remove(supply)
                    if len(in_set) == 0:
                        res.append(recipe)
                        del r_to_i[recipe]
                        q.append(recipe)

        return res



class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r_to_i = {
            recipes[i]: ingredients[i] for i in range(len(recipes)) 
        }
        
        supplies = set(supplies)
        seen = set()
        
        @cache
        def find_valid(recipe):
            if recipe in seen:
                return False
            seen.add(recipe)
            
            ingredient = r_to_i[recipe]
            
            for e in ingredient:
                if e not in supplies:
                    if e not in r_to_i:
                        return False
                    else:
                        if not find_valid(e):
                            return False

            return True

        res = []
        for recipe in recipes:
            if find_valid(recipe):
                res.append(recipe)

        return res
