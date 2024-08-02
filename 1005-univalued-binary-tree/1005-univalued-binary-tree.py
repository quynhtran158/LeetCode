# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check_value(node, value):
            if not node: #base case of the recursive call
                return True
            if node.val != value:
                return False
            return check_value(node.left, value) and check_value(node.right, value)
        
        return check_value(root, root.val)
