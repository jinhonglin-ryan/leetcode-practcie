class Solution(object):
    def __init__(self):
        self.p = [] # 并查集数组
        
        
    def find(self, x): # 返回x的根节点（路径压缩）
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # 无向图找环-->并查集
        # 遍历每条边，每遍历到一条边，相当于在这两个端点之间加一条边，也就是合并两个端点所在的集合 
        # 如果遍历到一条边，在加这条边之前，两个端点已经在同个集合内了，加完这条边之后就会形成环
        # 遍历边的时候从前往后遍历，这样输出的结果就是最后一次导致环出现的边
        
        
        # 总边数 = 总点数
        n = len(edges)
        # 并查集数组 初始化
        self.p = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            self.p[i] = i
            
        for e in edges:
            # a b分别为这条边的两个端点的祖宗节点
            a = self.find(e[0])
            b = self.find(e[1])
            
            if a != b: # 说明没有出现环，我们可以加这条边, 即合并两个集合
                self.p[a] = b
            else: # 否则 出现环， 直接return 这个边 
                return e
        return {}
                
        