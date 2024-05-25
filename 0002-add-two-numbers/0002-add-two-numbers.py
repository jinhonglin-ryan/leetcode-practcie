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
        
        dummy = ListNode()
        curr = dummy
        carry = 0
        
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
            
            sum_tmp = num_1 + num_2 + carry
            carry = sum_tmp // 10
            
            curr.next = ListNode(sum_tmp % 10)
            curr = curr.next
            
        return dummy.next
    