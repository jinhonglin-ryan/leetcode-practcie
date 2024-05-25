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
        
        # Method 1: set()
        
#         node_set = set()
#         curr = head
        
#         while curr:
#             if curr in node_set:
#                 return True
#             node_set.add(curr)
#             curr = curr.next
            
#         return False 
    
        
        # Method 2: 快慢双指针
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True