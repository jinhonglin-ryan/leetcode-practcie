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
            for j in range(num + (rem > 0)):  # 当 rem > 0 时，每部分多一个节点
                each.next = head
                each = each.next
                if head:
                    head = head.next
            if rem > 0:
                rem -= 1
            each.next = None
            res.append(dummy.next)

        return res 
            
    
                    
                
                
                
                                
    