# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        linked_list = []
        curr = head
        
        while curr:
            linked_list.append(curr)
            curr = curr.next 
        
        left = 0 
        right = len(linked_list) - 1
        
        while left < right: 
            linked_list[left].next = linked_list[right]
            left += 1
            if right == left:
                break
            linked_list[right].next = linked_list[left]
            right -= 1
            
        linked_list[left].next = None
        