# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
            
        num = length / k
        rem = length % k
        res = []
        
        for i in range(k):
            dummy = ListNode()
            each = dummy
            
            for j in range(num):
                node = ListNode(head.val)
                each.next = node
                each = each.next
                head = head.next
                
            if rem and head:
                nodex = ListNode(head.val)
                each.next = nodex
                head = head.next
                rem -= 1
                
            res.append(dummy.next)
            
        return res 
                
                
            
        