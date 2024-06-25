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
        
        self.dfs(node)
        
        for old, new in self.old_to_new.items():
            for neighbor in old.neighbors:
                new.neighbors.append(self.old_to_new[neighbor])
                
        return self.old_to_new[node]
    
    def dfs(self, node):
        self.old_to_new[node] = Node(node.val)
        
        for neighbor in node.neighbors:
            if neighbor not in self.old_to_new:
                self.dfs(neighbor)
       