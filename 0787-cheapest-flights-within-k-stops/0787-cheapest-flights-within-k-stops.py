class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        # 有边数限制的有向加权图单源最短路算法: Bellman-Ford算法：可以处理有负权边的数
        # 迭代n次，每一次循环所有边，a, b, w, 从a走到b的边加权为weight
        # 更新到b的最短路（dist[b] = min(dist[b], dist[a] + w)) 
        
        # 迭代n次的这个n是有意义的，比如迭代k次就是从起点出发，经过不超过k条边，走到每个点的距离
        # 这个思想可以用来找图中是不是有负环，迭代n次后，第n次迭代还有更新的话，说明存在一条最短路径，上面有n条边，如果一个路径上有n条边，意味着有n+1个点，但我们总共只有n个点，意味着其中有两个点的编号一样，意味着我们这条路径上存在一个负环（但是一般找负环的方法是spfa）如果有负权回路，最短路径不一定存在了
        
        # 题目中问要求at most k stops的最短路，也就是问at most k + 1 条边的最短路，所以我们要迭代k+1次
        
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        
        for i in range(k + 1):
            new_dist = dist[:]
            for u, v, w in flights:
                new_dist[v] = min(new_dist[v], dist[u] + w)
            dist = new_dist
            
        return -1 if dist[dst] == float('inf') else dist[dst]
        
        
        