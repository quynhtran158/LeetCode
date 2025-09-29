# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
plan:
because this is binary search tree, 
Start traversing the tree from the root node.
If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees.
and hence we return this common node as the LCA.

TC: worst case skewed tree (1 line) O(n), O(h) with h is height of the tree
SP: O(1)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        #iterative
        # while root:
        #     if root.val < min(p.val, q.val): #root.val < both p and q.val => LCA in right branch 
        #         root = root.right
        #     elif root.val > max(p.val, q.val):
        #         root = root.left
        #     else:
        #         return root

        #recursive
        
        parentVal = root.val
        pVal = p.val
        qVal = q.val

        if parentVal > max(pVal, qVal):
            return self.lowestCommonAncestor(root.left, p, q)
        elif parentVal < min(pVal, qVal):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
                
        
