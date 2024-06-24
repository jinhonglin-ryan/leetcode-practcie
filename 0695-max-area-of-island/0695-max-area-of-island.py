class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(x, y):
            # 检查当前坐标是否在网格范围内及是否为陆地
            if not (0 <= x < len(grid)) or not (0 <= y < len(grid[x])) or grid[x][y] != 1:
                return 0
            
            # 将当前陆地标记为已访问
            grid[x][y] = 0
            
            # 递归调用 dfs 检查上下左右四个方向，并累加面积
            # return 1 + 是因为当前是一个陆地，算面积为1
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
        
        # 初始化最大面积
        area = 0
        # 遍历网格的每个位置
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 如果当前坐标是陆地
                if grid[i][j] == 1:
                    # 调用 dfs 计算岛屿面积
                    res = dfs(i, j)
                    # 更新最大面积
                    area = max(area, res)
        # 返回最大岛屿面积
        return area
