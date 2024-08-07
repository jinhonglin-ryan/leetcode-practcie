# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        dummy.next = head 
        
        
        curr = dummy
        
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                temp = curr.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                
                curr.next = temp.next
                
            else:
                curr = curr.next
                
        return dummy.next 