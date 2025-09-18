# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
approach:
goal is take the tail of the LL as new head, then reverse the pointer (start from new head) 
use recursion: recurse until reach the tail of LL and take it as new head. break the LL into sub LL, slowly reverse the sub list except the current head. 

use circular poitner to reverse the pointer

if head null or only 1 node -> return the node

1 -> 2 -> null
|  <------ |


2 -> 1

head      new head

(head.next).next = head
2. next = head = 1

(rn: 1.next.next = null)


iterative:
approach:
- have prev = null as the end of new LL
- nxt as pointer to reverse LL
- next as pointer to move fwd in original LL
- move curr along head, curr.next = head. next
- move prev along curr after have nxt point point to the left (reverse)


prev = null
      head
     1 > 2 > 3
             ^curr
         prev

curr next: move to next node in original LL and reverse => will have 2 next
nxt to move to next node in original LL
next to reverse
prev = nul
curr.nxt = prev

  null < 1 < 2 < 3
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr.nextAttemp = curr.next
            curr.next = prev
            prev = curr
            curr = curr.nextAttemp
        return prev

