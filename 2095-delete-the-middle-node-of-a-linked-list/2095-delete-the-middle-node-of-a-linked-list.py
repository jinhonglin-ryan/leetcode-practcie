# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Method 2. 快慢指针做法，快指针每次走两步，慢指针每次走一步
        
        # Method 1. 暴力做法
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None
        
        mid_prev = (length // 2) - 1
        
        cnt = 0
        curr = head
        
        while cnt < mid_prev:
            curr = curr.next
            cnt += 1 
            
        curr.next = curr.next.next
        
        return head 