# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
iterative:
has dummy head point to a new node (-1), have 2 pointer for each LL, iterate thru 2LL, connect the smaller value to the dummy new node, continue adding smaleller node value after companring them 

both empty
either empty 

recursive:
just need to sort the first element from each LL, the rest will be break down and handle by recursion



'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(-1) #negative to prevent mixed with L1 L2 since they contain positive num only
        # curr = dummy

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next =list2
        #         list2 = list2.next
        #     curr = curr.next 
        # curr.next = list1 if list2 is None else list2
        # return dummy.next
        

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 
        else: #list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
            



