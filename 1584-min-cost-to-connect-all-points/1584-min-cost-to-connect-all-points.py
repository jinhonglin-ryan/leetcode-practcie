class Solution(object):
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def prim(self, points):
        size = len(points)
        visited = set() # 保存已经访问过的点
        dis = [float('inf') for _ in range(size)] # 储存每个点到集合的距离，初始化为正无穷
        
        ans = 0 # 最小生成树的weight sum 
        visited.add(0) # 从第一个节点开始生成, 第一个节点被标记已访问
        dis[0] = 0 # 从第一个节点开始生成，该节点到自己的距离为0
        
        # 将第一个点加入集合后，更新其他点到集合的最小距离
        for i in range(1, size):
            dis[i] = self.distance(points[0], points[i])
            
        # 我们一共需要加入size个点来构建MST, 目前加入了一个点，所以还需要遍历size-1次
        for _ in range(size - 1):
            min_dis = float('inf')
            min_dis_i = -1
            
            # 遍历所有点，找出不在集合中的点到集合的最小距离以及最小距离的index
            for i in range(size):
                if i not in visited and dis[i] < min_dis:
                    min_dis = dis[i]
                    min_dis_i = i
                    
            # if min_dis_i == -1:
            #     return
            
            # 把最小距离加入ans，和标记当前找到的到集合最小距离的点为访问过
            ans += min_dis
            visited.add(min_dis_i)
            
            # 更新其他点到集合的最小距离
            for i in range(size):
                if i not in visited:
                    dis[i] = min(dis[i], self.distance(points[i], points[min_dis_i]))
                    
        return ans
            
 
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return self.prim(points)