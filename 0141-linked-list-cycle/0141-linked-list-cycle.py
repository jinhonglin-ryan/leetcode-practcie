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
        
        all_set = set()
        
        curr = head 
        
        while curr:
            if curr in all_set:
                return True
            all_set.add(curr)
            curr = curr.next
        return False 