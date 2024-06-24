class Solution(object):
    def __init__(self):
        self.g = None
        self.count = 0
        
    def dfs(self, x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        self.g[x][y] = 0
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if (a >= 0 and a < len(self.g) and b >= 0 and b < len(self.g[a]) and self.g[a][b] == '1'):
                self.dfs(a, b)
                
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # flood fill算法
        # dfs实现
        self.g = grid
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                if self.g[i][j] == '1':
                    self.dfs(i, j)
                    self.count += 1
        return self.count