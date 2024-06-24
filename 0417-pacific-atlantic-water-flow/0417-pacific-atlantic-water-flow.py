class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 思路：
        # 从太平洋的边界和大西洋的边界分别出发dfs，记录下分别能到的坐标点
        # 最后遍历整个grid把重复的坐标点取出作为答案返回
        
        # dfs的逻辑：通过递归遍历每个节点及其四个方向的邻居节点，标记所有可以流向太平洋或大西洋的节点。通过从边界点开始进行 DFS，逐步标记所有可以流到太平洋和大西洋的区域，最终确定哪些位置可以同时流向两大洋。
        
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        def dfs(x, y, visited):
            visited[x][y] = True
            
            # 对于当前点的四个方向进行遍历
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                
                # 如果走了这个方向后不在grid内，进入下一次循环
                if not 0 <= a < rows or not 0 <= b < cols:
                    continue
                # 如果这个方向是valid的，去验证heights是否比原先的高
                # 如果是，且这个方向没有被遍历过，对这个方向进行dfs
                if heights[a][b] >= heights[x][y] and not visited[a][b]:
                    dfs(a, b, visited)
        
        # 从太平洋和大西洋的边界开始dfs
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)
            
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i, j])
        return res 
        
        
        