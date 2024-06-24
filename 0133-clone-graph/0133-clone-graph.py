# 定义节点类
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def __init__(self):
        # 字典用于记录旧节点到新节点的映射
        self.old_to_new = {}
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        
        # 深度优先搜索复制所有节点
        self.dfs(node)
        
        # 将旧节点的邻居复制到新节点
        for old_node, new_node in self.old_to_new.items():
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(self.old_to_new[neighbor])
        
        # 返回新图的起始节点
        return self.old_to_new[node]
    
    def dfs(self, node):
        # 创建新节点并记录在字典中
        self.old_to_new[node] = Node(node.val)
        
        # 递归地复制邻居节点
        for neighbor in node.neighbors:
            if neighbor not in self.old_to_new:
                self.dfs(neighbor)
