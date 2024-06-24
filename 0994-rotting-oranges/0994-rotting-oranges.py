class Solution(object):
    def __init__(self):
        self.ans = 0
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # BFS的思想
        # 先将所有腐烂橘子存入队列，然后开始bfs
        
        queue = deque()
        minutes = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                  
        if queue:
            minutes -= 1
            
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft() # 取出一个腐烂的橘子
                for i in range(4): # 在这个腐烂橘子的四个方向找未腐烂的橘子 
                    a = x + dx[i]
                    b = y + dy[i]
                    # 如果在边界内且未腐烂
                    if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1:
                        grid[a][b] = 2
                        queue.append((a,b)) # 将这个腐烂的橘子加入队列
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # 如果全部腐烂完了之后，还存在未腐烂的橘子，返回-1
                    return -1
                
        return minutes
                    
            