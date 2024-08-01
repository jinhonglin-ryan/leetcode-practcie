# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # bfs：需要queue
        if root is None:
            return None
        
        # res 用于存储整个树的层序遍历结果
        res = []
        
        # queue 用于按顺序存储待处理的树节点
        queue = [root]
        
        while queue:
            # 用于存储当前层的所有节点的值
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                # 保证了下一层的节点将在下一个大循环中按顺序处理
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right) 
                
            if level:
                res.append(level)
        return res