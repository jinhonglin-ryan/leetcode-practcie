# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        head = ListNode()
        curr = head
        
        while l1 or l2 or carry:
            if l1:
                num_1 = l1.val
                l1 = l1.next
            else:
                num_1 = 0
            
            if l2:
                num_2 = l2.val
                l2 = l2.next
            else:
                num_2 = 0
            
            sum_curr = num_1 + num_2 + carry
            carry = sum_curr // 10 
            
            curr.next = ListNode(sum_curr % 10)
            curr = curr.next
            
        return head.next 
            
        