# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
binary no left smaller than node, right bigger than node
all node.val distinct value? yes
guarantee q, p exist? => means tree not null?

plan:
- find the first node the has each node in each sub tree (1st node see both p and q)
- the LCA only have 1 q or p in each subtree, cannot have both q and p in 1 subtree -> if have both q and p if fall into other case
- if in 1 subtree has both q and p means that the LCA is either q or p


'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root in (None, q, p):
            return root

        leftSub = self.lowestCommonAncestor(root.left, q, p) #recursively all left sub, only stop when root meet q/p or none
        rightSub = self.lowestCommonAncestor(root.right, q, p) #after run recursion of leftSub, run this rightSub 

        if leftSub is not None and rightSub is not None:
            return root
        return leftSub or rightSub #return left because left will be detecy fi




        
