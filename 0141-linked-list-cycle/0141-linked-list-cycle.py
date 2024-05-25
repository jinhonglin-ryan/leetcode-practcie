# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        count = {}
        
        curr = head
        
        while curr:
            if curr in count:
                return True
            else:
                count[curr] = 1
            curr = curr.next 
        return False
            