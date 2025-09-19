# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
combine the number in each node into a number, then reverse them then sum 2 number, then return them as a LL of number
one 1 digit per node -> 6 + 4 = 0 carry 1 to the next node

return the sum as LL

approach:
calc the sum of 2 LL as it is (reversed), have variable call carry for case sum > 9, then add the carry to the next sum 
have a dummy node, then dummy.next point to the first node of the sum, after the calculation, add the sum as a new node
return need to return dummy.next, to return the LL represent the sum 

2 > 4 > 3

5 > 6 > 4

x 2
y 5
car= (x+y)//10 (9+9 = 18 -> 1) -> 1 bc of int
sum = (x + y + car) % 10 | mod 10 để lấy số hàng đơn vi
(reset car) car = 0


 
0 > 7 > 0 > 8
^dummy   
    ^curr     
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) #need dummy node bc the LL doesn't not exit yet
        curr = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            colSum = l1Val + l2Val + carry
            carry = colSum // 10 
            newNode = colSum % 10
            curr.next = ListNode(newNode) #at first, curr point to 0, curr.next set the pointer from node 0 to node 7, dummy never change sp return dummy.next will return node 7 
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        


                

        