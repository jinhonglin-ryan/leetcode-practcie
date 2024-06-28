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
        
        for e in times:
            u = e[0]
            v = e[1]
            t = e[2]
            
            graph[u].append([v, t])
            
        dist = self.dijkstra(graph, k, n)
        max_dist = 0
        
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            max_dist = max(max_dist, dist[i])
        return max_dist
    
    
    def dijkstra(self, graph, start, n):
        
        dist = [float('inf') for _ in range(n + 1)]
        
        dist[start] = 0
        
        queue = deque()
        queue.append([start, 0])
        
        while queue:
            v, time = queue.popleft()
            if time > dist[v]:
                continue
            
            dist[v] = time
            
            if graph[v] == []:
                continue
            
            for e in graph[v]:
                q = e[0]
                t = e[1]
                
                if dist[q] > t + time:
                    dist[q] = t + time
                    queue.append([q, dist[q]])
        return dist
            
            