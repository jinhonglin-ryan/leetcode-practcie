class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        cnt = 0
        
        rows = defaultdict(int)
        
        for row in grid:
            rows[tuple(row)] += 1
            
        for i in range(n):
            col = [grid[r][i] for r in range(n)]
            cnt += rows[tuple(col)]
            
        return cnt 