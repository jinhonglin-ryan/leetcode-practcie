# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            curr = prev.next
            next_node = curr.next
            
            curr.next = next_node.next
            next_node.next = curr
            prev.next = next_node
            
            prev = curr
        
        return dummy.next 