class Solution(object):
    # Dijkstra算法
    # 求单源最短路径，即从一个指定起点（源点）到图中其他所有顶点的最短路径。
    # 适用于加权图，但要求图中的边权重为非负值。
    # 通过贪心策略，不断选择当前最短路径的顶点，并更新与之相邻的顶点的最短路径。
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = defaultdict(list)
        
        for u, v, t in times:
            graph[u].append((v, t))
        
        distance = self.dijkstra(graph, n, k)
        max_dist = max(distance.values())
        return max_dist if max_dist < float('inf') else -1
    
    
    def dijkstra(self, graph, n, start):
        # Priority queue: (distance, node)
        pq = [(0, start)]
        dist = {i: float('inf') for i in range(1, n + 1)} # 记录从起点出发到每个点到最小距离
        dist[start] = 0
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > dist[u]:
                continue
            
            for v, time in graph[u]:
                new_dist = current_dist + time
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        return dist
        
        
        
    
#     def networkDelayTime(self, times, n, k):
#         """
#         :type times: List[List[int]]
#         :type n: int
#         :type k: int
#         :rtype: int
#         """
#         # 初始化图
#         # graph这个dictionary 存的是从key出发可以到哪些点，花费时间是多少
#         # 到哪些点是value[0]，到该点花费时间是value[1]
#         # graph[u] 存储从节点 u 出发可以到达的节点 v 及其对应的权重 t。
#         graph = defaultdict(list)
#         for e in times:
#             u = e[0]
#             v = e[1]
#             t = e[2]
            
#             graph[u].append([v, t])
        
#         # 计算从起点 k 到所有节点的最短路径，返回的 dist 数组表示从起点到每个节点的最短路径长度。
#         dist = self.dijkstra(graph, k, n)
        
#         max_dist = 0
#         for i in range(1, n + 1):
#             if dist[i] == float('inf'): # 如果某个节点的最短路径是无穷大，说明我们没有更新到这个节点，仍然是初始的无穷大值，说明该节点无法到达，返回 -1。
#                 return -1
#             max_dist = max(dist[i], max_dist)
#         return max_dist
    
    
#     def dijkstra(self, graph, start, n):
#         dist = [float('inf') for _ in range(n + 1)] # 先初始化dis，存放从起点到该点到最短距离 
#         # queue表示对到某一个点的距离进行修改后，需要把这个点取出，从当前节点出发，尝试更新到其他点的最短距离
#         queue = deque()
        
#         # 从起点到起点到最短距离是0
#         dist[start] = 0
        
#         queue.append([start, 0])
        
#         while queue:
#             target, time = queue.popleft()
#             # 如果当前到target所需要的时间大于已知的到target所需要的最短时间，跳过
#             if time > dist[target]:
#                 continue 
            
#             # 否则 更新到target的最短时间为当前时间
#             dist[target] = time
            
#             # 如果当前target没有指向的节点，跳过
#             if graph[target] == []:
#                 continue
            
#             for e in graph[target]: # 遍历当前节点的所有邻接点
#                 v = e[0]
#                 t = e[1]
#                 if (dist[v] > t + time): # 如果从当前节点到邻接点的路径长度小于已知的最短路径长度，更新 dist[v]。
#                     dist[v] = t + time 
#                     # 并且将这个节点加入队列，晚点需要pop出来来更新从这个节点出发到别的节点的最短路径
#                     queue.append([v, dist[v]])
                
#         return dist
        
        