class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(x, y):
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[x]) or grid[x][y] != 1:
                return 0
            
            grid[x][y] = 0
            
            return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = dfs(i, j)
                    area = max(area, res)
        return area