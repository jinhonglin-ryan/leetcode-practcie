class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # 有向图的拓扑排序：有拓扑序 == 图中一定不存在环
        # 拓扑排序
        # 1. 统计每个点有多少条边指向它
        # 入度为0表示我们可以直接走
        # 2. 将所有入度为0的点加入队列
        # 队列维护的是当前入度为0的点
        # 3. BFS 取出当前队列中的随机一个点（入度为0）
        # 更新这个点的后继节点，入度-1，如果后继节点-1后入度为0，则加入队列
        
        edges = prerequisites
        n = numCourses
        
        # 定义邻接表
        g = defaultdict(list)
        d = defaultdict(int)
        for e in edges:
            a = e[0]
            b = e[1]
            
            g[a].append(b)
            d[b] += 1
        
        # 定义队列, 把所有入度为0的点加入队列
        queue = deque()
        
        for i in range(n):
            if d[i] == 0:
                queue.append(i)
        
        count = 0 
        while queue:
            t = queue.popleft()
            count += 1
            for i in g[t]:
                d[i] -= 1
                if d[i] == 0:
                    queue.append(i)
        
        return count == n 