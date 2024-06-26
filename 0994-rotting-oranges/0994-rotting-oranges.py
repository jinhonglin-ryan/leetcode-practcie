class Solution(object):
    def __init__(self):
        self.ans = 0
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # BFS的思想，找需要多少层来腐烂全部的橘子
        # 先将所有腐烂橘子存入队列，这个作为第一层，然后开始bfs
        # 从队列中取出某层中的每一个腐烂的橘子 然后考虑其四个方向，如果有未腐烂的橘子，就会把他腐烂然后加入队列中，当一层腐烂的橘子全部被取出后，队列中的是下一层腐烂的橘子
        
        
        # 注意一开始要先让 minutes - 1
        # 因为我们初始化队列后，如果队列中有至少一层腐烂的橘子，这是原先已经被腐烂了的，不需要花时间去腐烂，所以要minutes - 1
        # 假设我们现在只有一个腐烂的橘子，周围有一层未腐烂的橘子，那么实际上只需要1分钟就可以腐烂完成
        # 如果minutes一开始是0， 那么我们进入while queue之后，minutes 变成1，然后我们取出那些未腐烂的橘子腐烂，加入queue之后又进到下一次while queue循环，minutes变成2，然后遍历发现没有未腐烂的橘子了，while退出，最后minutes是2，所以我们需要一开始minutes-1 来保证结果的正确
        
        
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
            size = len(queue)
            for _ in range(size):
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
                    
            