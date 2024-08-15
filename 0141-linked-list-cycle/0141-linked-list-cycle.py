# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        if head is None:
            return None
        
        curr = head
        while head and head.next: #LL has at least 2 nodes
            if count != pos:
                head = head.next
                count += 1
            else:
                while curr.next != head:
                    curr = curr.next 
                return True
        return False

            
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        curr_head = head
        tail = head
        
        while tail and tail.next: # LL has at least 2 nodes
            curr_head = curr_head.next
            tail = tail.next.next
            
            if curr_head == tail:
                return True
        return False