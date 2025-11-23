# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Do a bfs, level by level traversal using a q
        use a boolean to keep track of the zig zag and the way we add the order into the result
        """
        res = []
        if not root: return res

        q = deque([root])
        odd = True

        while q:
            size = len(q)
            current = []
            for _ in range(size):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if odd:
                res.append(current)
            else:
                res.append(current[::-1])
            odd = not odd
        
        return res
