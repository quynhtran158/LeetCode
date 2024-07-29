# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 1
        # minLevel = float('inf') ->
        d = deque([root])
        if not root:
            return 0
        while d:
            for i in range(len(d)):
                node = d.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            level += 1
            # minLevel = min(level, minLevel) no need to have minLvl bc we return the level immediately when we reach the leaf node
        return minLevel