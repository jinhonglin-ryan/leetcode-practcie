# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        odd_head = ListNode()
        even_head = ListNode()
        
        odd = odd_head
        even = even_head
        curr = head
        
        i = 1
        
        while curr:
            if i % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
                
            curr = curr.next
            i += 1
            
        # 将最后一个偶数节点的next指向None以防形成环
        even.next = None
        # 将奇数链表的末尾连接到偶数链表的头部
        odd.next = even_head.next
        
        return odd_head.next

        
        
            
        
        
        