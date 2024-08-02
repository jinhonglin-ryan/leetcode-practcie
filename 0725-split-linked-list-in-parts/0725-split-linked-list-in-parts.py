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
            cnt += 1
            curr = curr.next
            
        x = cnt / k
        remaining = cnt % k
        
        for i in range(k):
            dummy = ListNode()
            curr = dummy
            for j in range(x):
                node = ListNode(head.val)
                curr.next = node
                curr = curr.next
                head = head.next
                
            if remaining and head is not None:
                node = ListNode(head.val)
                curr.next = node
                if head is not None:
                    head = head.next
                remaining -= 1
            res.append(dummy.next)
            
        return res
    
                    
                
                
                
                                
    