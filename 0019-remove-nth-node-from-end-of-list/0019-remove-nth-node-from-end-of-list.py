# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        k = 0 
        curr = head
        while curr is not None:
            k += 1
            curr = curr.next
        
        if k == 1 and n == 1:
            head = None
            return head
        
        # k is the length of the linked list k = 2 n = 2
        if k == n:
            return head.next 
        
        curr = head
        while k > n + 1 and curr is not None:
            curr = curr.next
            k -= 1
        if curr is None:
            return head
        
        if curr.next is None:
            return head
        
        if curr.next.next is None:
            curr.next = None
            return head
        
        tmp = curr.next.next
        curr.next = tmp
        return head