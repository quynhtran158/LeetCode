# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    empty tree?
    - find the max left depth node, and max right depth node of each node, then calculate the max sum of left and right
    '''
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0  # Local variable to track the maximum diameter
        
        # Helper function to calculate the max depth of a subtree
        def maxDepth(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter  # Declare maxDiameter as nonlocal to modify it
            # Base case: if node is None, the depth is 0
            if not node:
                return 0

            # Recursively calculate the depth of left and right children
            leftDepth = maxDepth(node.left)
            rightDepth = maxDepth(node.right)

            # Update the maximum diameter found so far
            maxDiameter = max(maxDiameter, leftDepth + rightDepth)

            # The depth of the current node is 1 + the maximum of the depths of its children
            return 1 + max(leftDepth, rightDepth)
        
        # Call the helper function to calculate the depth and update the diameter
        maxDepth(root)

        # Return the maximum diameter found
        return maxDiameter