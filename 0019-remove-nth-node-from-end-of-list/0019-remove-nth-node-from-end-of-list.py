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
    
#         # Method 2：yxc 方法，类似，但是更精简
#         k = 0 
#         # dummy节点 处理删除头节点的特殊情况 
#         dummy = ListNode()
#         dummy.next = head
#         curr = head
#         while curr is not None:
#             k += 1
#             curr = curr.next
        
#         # 要删除倒数第n个点，我们需要找到倒数第n+1个点
#         # 意思就是从第一个数开始，需要移动k - n - 1步 才能到倒数n+1个点
#         # 所以从dummy开始，需要多移动一步，也就是k-n步 
#         # 找到倒数第n+1个点之后，删除第n个点就很方便了
#         # k = 5, n = 2
#         index = 0
#         temp = dummy 
#         for index in range(0, k - n):
#             temp = temp.next
#         temp.next = temp.next.next
        
#         return dummy.next 
    
        # Method 3: 快慢双指针
        # 先将快指针往前走n步
        # 然后快慢指针一起走，直到快指针走到null了之后停止
        # 这时候慢指针指向要被删除节点的前一个node
        # 然后正常删除操作即可
        # 也用dummy来handle删除头节点的情况
        
        dummy = ListNode()
        dummy.next = head
        
        fast = head
        slow = dummy
        while n:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next 
            
        
        
            
        
        
        