"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head is None:
            return None
        
        
        old_new_dict = {}
        
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            old_new_dict[curr] = new_node
            curr = curr.next 
        
        curr = head
        while curr:
            if curr.next:
                old_new_dict[curr].next = old_new_dict[curr.next]
            if curr.random:
                old_new_dict[curr].random = old_new_dict[curr.random]
            curr = curr.next
            
        return old_new_dict[head]
            