# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, tree: Optional[TreeNode], target: float) -> int:
        if not tree:
            return None

        queue = deque([tree])
        closest = tree.val

        while queue:
            node = queue.popleft()

            if abs(target - node.val) < abs(target - closest) or \
   (abs(target - node.val) == abs(target - closest) and node.val < closest):
                closest = node.val

            # Prioritize the correct child based on BST properties
            if target < node.val and node.left:
                queue.append(node.left)
            elif target > node.val and node.right:
                queue.append(node.right)

        return closest