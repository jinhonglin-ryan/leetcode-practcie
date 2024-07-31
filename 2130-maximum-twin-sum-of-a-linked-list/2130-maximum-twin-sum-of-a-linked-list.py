# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        res = 0
        length = 0
        
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
            
        mid = length // 2
        
        i = 0
        left = []
        right = []
        
        curr = head
        
        while curr:
            if i < mid:
                left.append(curr.val)
            else:
                right.append(curr.val)
            
            curr = curr.next
            i += 1
            
        right = right[::-1]
        
        for i in range(mid):
            total = left[i] + right[i]
            res = max(res, total)
        
        return res 