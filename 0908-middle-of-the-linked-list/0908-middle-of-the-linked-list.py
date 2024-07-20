# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # if head is None:
#         #     return None
        
#         current = head
#         len = 0
#         curr_len = 0
#         while current:
#             current = head.next
#             len += 1

#             if len % 2 !=0:
#                 while current and curr_len != (len/2):
#                     current = head.next
#                     curr_len += 1
#                 return current
#             else:
#                 while current and curr_len != (len/2)+1:
#                     current = head.next
#                     curr_len += 1
#                 return current
        
             
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # Step 2: Find the middle node
        current = head
        mid = length // 2
        for _ in range(mid):
            current = current.next
        
        return current

