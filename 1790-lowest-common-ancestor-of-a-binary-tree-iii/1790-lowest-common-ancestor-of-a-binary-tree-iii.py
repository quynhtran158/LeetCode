"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
'''
technically, the lowest ancestor is the closest common parent of both node compare to both nodes but furthest compare to root node

clarify
-guarantee always has q, p in tree -> yes then tree will always exist
- all node value are unique? yes => if no, how to know which node is the one we want?

plan:
Find the depth of each pointer
Move the deeper pointer up until it is at the same level as the other pointer
Move each pointer up level-by-level until they meet
'''

class Solution:
    def get_depth(self, p): #walks up the tree from node p to the root.
		# helper function to find the depth of the pointer in the tree
        depth = 0
        while p: ##When p becomes None, you’ve passed the root.
            p = p.parent ##move p up to p's parent node
            depth += 1 ##count the step it taks
        return depth ##Returns how far down the tree the node is.
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node': ## pase the node object alr so we know the exact position of the node. No need to find and dinh vi cai node ow dauy

		# find the depth of each pointer
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
		
		# Move the lower pointer up so that they are each at the same level. 
		# For the smaller depth (p_depth < q_depth or q_depth < p_depth), 
		# the loop will be skipped and the pointer will stay at the same depth.
        for _ in range(p_depth - q_depth): ## only runs if p is deeper, range (-2) -> 0:-2, doesnt exist so simply skip
            p = p.parent
        for _ in range(q_depth - p_depth): ## only runs if q is deeper, range (-2) -> 0:-2, doesnt exist so simply skip
            q = q.parent
        
		# Now that they are at the same depth, move them up the tree in parallel until they meet
        while p != q:
            p=p.parent
            q=q.parent
        return p