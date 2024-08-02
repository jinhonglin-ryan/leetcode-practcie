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
        
        res = []
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        
        num = cnt / k
        rem = cnt % k
        
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
            
    
                    
                
                
                
                                
    