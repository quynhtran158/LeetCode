from collections import deque, defaultdict
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        def can_make_recipes(recipes, ingredients, supplies):
            res = []
            q = deque(supplies)  # Queue to store available ingredients
            available = set(supplies)  # Set to track available ingredients (both initial supplies and recipes that can be made)
            
            graph = defaultdict(list)
            indegree = {recipe: 0 for recipe in recipes}

            # Build graph and initialize indegrees
            for i in range(len(recipes)):
                recipe = recipes[i]
                ing_list = ingredients[i]
                for ingredient in ing_list:
                    if ingredient not in available:
                        graph[ingredient].append(recipe)  # Add edges from ingredient to recipe
                        indegree[recipe] += 1
            
            # Perform BFS to topologically sort and find recipes we can make
            while q:
                current = q.popleft()
                
                # Process each recipe that depends on the current ingredient
                for i in range(len(recipes)):
                    recipe = recipes[i]
                    ing_list = ingredients[i]
                    if recipe not in available:
                        if all(ingredient in available for ingredient in ing_list):
                            available.add(recipe)
                            q.append(recipe)
                            res.append(recipe)
            
            return res
        
        # Call the helper function to get the list of recipes we can make
        return can_make_recipes(recipes, ingredients, supplies)
