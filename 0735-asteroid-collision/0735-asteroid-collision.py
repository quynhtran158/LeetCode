class Solution:
    '''
    - is this asteroids always postitive in the left and negative in the right?
    
    - all positive
    - all negative
    - 

    the positive and negative asteroids must be next to each other 
    
    plan:
    - all negative/postitive -> no collision
    - if collision happens: ast < 0 (move to left), stack[-1] > 0 (move to right)
        make sure the stack is available (has at least one element in the stack)
            - ast < top, no append
            - ast > top, pop top, append ast
            - ast = top, pop top 
        
        

    '''

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if -ast == stack[-1]:
                    stack.pop()
                    break
                elif -ast > stack[-1]:
                    stack.pop()
                    # stack.append(ast)
                else:
                    break
            #no collision appears
            else:
                stack.append(ast)
        
        return stack

            
