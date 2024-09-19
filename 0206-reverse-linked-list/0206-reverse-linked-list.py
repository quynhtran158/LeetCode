# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr: #didnt reach the end of LL
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt 
        return prev #bc prev is the new head of the LL
