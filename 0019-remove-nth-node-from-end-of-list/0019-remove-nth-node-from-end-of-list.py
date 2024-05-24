# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
#         # Method 1: 屎山代码 本人原创
#         k = 0 
#         curr = head
#         while curr is not None:
#             k += 1
#             curr = curr.next
        
#         if k == 1 and n == 1:
#             head = None
#             return head
        
#         # k is the length of the linked list
#         if k == n:
#             return head.next 
        
#         curr = head
#         while k > n + 1 and curr is not None:
#             curr = curr.next
#             k -= 1
            
#         if curr is None:
#             return head
        
#         if curr.next is None:
#             return head
        
#         if curr.next.next is None:
#             curr.next = None
#             return head
        
#         tmp = curr.next.next
#         curr.next = tmp
#         return head
    
        # Method 2：yxc 方法，类似，但是更精简
        k = 0 
        dummy = ListNode()
        dummy.next = head
        curr = head
        while curr is not None:
            k += 1
            curr = curr.next
        
        # 要删除倒数第n个点，我们需要找到倒数第n+1个点
        # 意思就是从第一个数开始，需要移动k - n - 1步 才能到倒数n+1个点
        # 找到倒数第n+1个点之后，删除第n个点就很方便了
        # k = 5, n = 2
        index = 0
        temp = dummy 
        for index in range(0, k - n):
            temp = temp.next
        temp.next = temp.next.next
        
        return dummy.next 
            
        
        
        