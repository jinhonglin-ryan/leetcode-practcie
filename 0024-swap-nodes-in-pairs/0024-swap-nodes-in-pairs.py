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
        
        # 只有当这两个节点都存在时，我们才有一对需要交换的节点
        # 每次循环处理一对节点，然后将 prev 指针移动到这对节点之后，即交换过的第二个节点的位置，为处理下一对节点做准备。
        while prev.next and prev.next.next:
            curr = prev.next
            next_node = curr.next 
            
            # swap
            curr.next = next_node.next
            next_node.next = curr 
            # prev指的是当前交换对的前一个node，所以prev.next要指向交换完成后的那个node
            prev.next = next_node
            
            
            # 在交换之后，原来的 curr 节点现在是这对节点中的第二个节点。因此，将 prev 更新为 curr，这样在下一次循环中，prev.next 将指向新的 curr，即下一对待交换节点的第一个节点。
            prev = curr
            
        return dummy.next 