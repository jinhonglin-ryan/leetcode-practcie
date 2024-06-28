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
        # 初始化图
        # graph这个dictionary 存的是从key出发可以到哪些点，花费时间是多少
        # 到哪些点是value[0]，到该点花费时间是value[1]
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
            max_dist = max(dist[i], max_dist)
        return max_dist
    
    def dijkstra(self, graph, start, n):
        dist = [float('inf') for _ in range(n + 1)] # 先初始化dis，存放从起点到该点到最短距离 
        # queue表示对到某一个点的距离进行修改后，需要把这个点取出，更新到其他点到距离
        queue = deque()
        
        # 从起点到起点到最短距离是0
        dist[start] = 0
        
        queue.append([start, 0])
        
        while queue:
            target, time = queue.popleft()
            # 如果当前到target所需要的时间大于已知的到target所需要的时间，跳过
            # 或者target没有指向别的点了，则不需要更新别的点的最短路经，跳过 
            if time > dist[target] or graph[target] == []:
                continue 
            
            dist[target] = time
            
            for e in graph[target]:
                v = e[0]
                t = e[1]
                if (dist[v] > t + time):
                    dist[v] = t + time 
                    queue.append([v, dist[v]])
                
        return dist
        
        