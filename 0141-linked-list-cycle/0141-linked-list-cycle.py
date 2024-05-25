# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # Method 1: set()
        
#         node_set = set()
#         curr = head
        
#         while curr:
#             if curr in node_set:
#                 return True
#             node_set.add(curr)
#             curr = curr.next
            
#         return False 
    
        
        # Method 2: 快慢双指针
        # 如果list为null或者只有一个node，肯定没有环，return false 
        if not head or not head.next:
            return False
        # 设置快慢双指针，初始化将两个指针错开
        # 快指针每次走两步，慢指针每次走一步
        # 因此如果有环，快指针和慢指针肯定最终会相遇，因为相对速度为1，有环的话，每次迭代，快慢指针之间的距离缩减1
        # 如果没有环的话，快指针会先走到null，那么就return false 表示没有环
        slow = head
        fast = head.next
        
        # 写法1：
        # 在while里面check if not fast or not fast.next:
        # 这是为了保证fast = fast.next.next 不会报错（不会是None.next.next or None.next），如果fast 或者fast.next是null了，说明没有环。return False
#         while slow != fast:
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
        
#         # 如果slow == fast 直接返回true
#         return True
        
        # 写法2：
        
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False
        # Method 3: 哈希表
#         node_to_count = {}
        
#         curr = head
#         while curr:
#             if curr in node_to_count:
#                 return True
#             else:
#                 node_to_count[curr] = 1
#             curr = curr.next
#         return False 