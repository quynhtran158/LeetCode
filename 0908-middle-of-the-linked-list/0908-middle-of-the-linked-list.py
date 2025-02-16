# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
what to return when the LL is null?
we use fast and slow pointer to find the middle of LL

odd
0 1 2 3 4 
    s 
        f
even
0 1 2 3 null
    s
        f 
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return null
        fast = slow = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        return slow
