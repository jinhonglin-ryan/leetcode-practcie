# class Solution(object):
#     def distance(self, a, b):
#         return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
#     def prim(self, points):
#         size = len(points)
#         visited = set() # 保存已经访问过的点
#         dis = [float('inf') for _ in range(size)] # 储存每个点到集合的距离，初始化为正无穷
        
#         ans = 0 # 最小生成树的weight sum 
#         visited.add(0) # 从第一个节点开始生成, 第一个节点被标记已访问
#         dis[0] = 0 # 从第一个节点开始生成，该节点到自己的距离为0
        
#         # 将第一个点加入集合后，更新其他点到集合的最小距离
#         for i in range(1, size):
#             dis[i] = self.distance(points[0], points[i])
            
#         # 我们一共需要加入size个点来构建MST, 目前加入了一个点，所以还需要遍历size-1次
#         for _ in range(size - 1):
#             min_dis = float('inf')
#             min_dis_i = -1
            
#             # 遍历所有点，找出不在集合中的点到集合的最小距离以及最小距离的index
#             for i in range(size):
#                 if i not in visited and dis[i] < min_dis:
#                     min_dis = dis[i]
#                     min_dis_i = i
                    
#             # if min_dis_i == -1:
#             #     return
            
#             # 把最小距离加入ans，和标记当前找到的到集合最小距离的点为访问过
#             ans += min_dis
#             visited.add(min_dis_i)
            
#             # 更新其他点到集合的最小距离
#             for i in range(size):
#                 if i not in visited:
#                     dis[i] = min(dis[i], self.distance(points[i], points[min_dis_i]))
                    
#         return ans
            
 
#     def minCostConnectPoints(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         return self.prim(points)


import heapq

class Solution(object):
    def prim(self, graph, start):
        """
        通用的Prim算法
        :param graph: 图的邻接表表示，格式为 {节点: [(邻居, 权重), ...]}
        :param start: 起始节点
        :return: 最小生成树的总权重
        """
        size = len(graph)
        visited = set()
        min_heap = [(0, start)]  # (边的权重, 节点)
        total_weight = 0
        
        while len(visited) < size: # 构建MST我们需要n个节点，所以只要visited的长度=n说明我们已经构建好MST了
            weight, u = heapq.heappop(min_heap) # 取出当前堆中node到集合的最小距离
            
            if u in visited:
                continue
            
            visited.add(u)
            total_weight += weight
            
            for v, edge_weight in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (edge_weight, v))
        
        return total_weight
    
    def minCostConnectPoints(self, points):
        """
        特定问题的Prim算法，用于计算连接所有点的最小成本
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        # 构建无向图的邻接表
        graph = defaultdict(list)
        size = len(points)
        for i in range(size):
            for j in range(i + 1, size):
                dist = distance(points[i], points[j])
                graph[i].append((j, dist))
                graph[j].append((i, dist))
        
        # 调用通用的Prim算法
        return self.prim(graph, 0)


