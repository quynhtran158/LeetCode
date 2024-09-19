# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    - empty LL? return?
    - 1 node -> return true
    
    plan:
    1) find the middle of the LL
    2) reverse the 2nd half of the LL
    3) compare the 1st and the 2nd half of the LL 

    '''

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # If the list is empty or has only one node, it's a palindrome
            return True
        slow = head
        fast = head
        #initilize fast and slow pointer to find the middle of the LL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         #slow is the middle of LL

        #reverse the 2nd half of LL 
        prev = None
        curr = slow
        while curr:
            #store the next node
            nxt = curr.next
            #update the pointer to reverse
            curr.next = prev
            #move prev fwd
            prev = curr
            #move currR fwd
            curr = nxt
        
        #traverse from start to middle and compare with the 2nd half of LL
        first_half = head
        second_half = prev
        while second_half and first_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True




            