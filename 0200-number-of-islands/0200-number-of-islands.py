class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def dfs(x, y):
            if not 0<=x<len(grid) or not 0<=y<len(grid[x]) or grid[x][y] != '1':
                return
            
            grid[x][y] = '2'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count