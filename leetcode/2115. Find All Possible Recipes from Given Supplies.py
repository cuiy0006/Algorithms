class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r_to_i = {
            recipes[i]: ingredients[i] for i in range(len(recipes)) 
        }
        
        supplies = set(supplies)
        non_exist = set()
        
        def find_valid(recipe, seen):
            if recipe in non_exist:
                return False
            if recipe in supplies:
                return True
            if recipe in seen:
                non_exist.add(recipe)
                return False
            
            seen.add(recipe)
            ingredient = r_to_i[recipe]
            
            for e in ingredient:
                if e not in supplies:
                    if e not in r_to_i:
                        non_exist.add(e)
                        return False
                    else:
                        if not find_valid(e, seen):
                            non_exist.add(recipe)
                            return False

            supplies.add(recipe)
            return True
    
        res = []
        for recipe in recipes:
            if find_valid(recipe, set()):
                res.append(recipe)

        return res
