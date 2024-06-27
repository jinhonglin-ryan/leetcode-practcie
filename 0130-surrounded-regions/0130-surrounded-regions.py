class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # 思路
        # 先遍历board的四个边界，把边界能走到的O全部打上标记，用dfs，这些并不是被包围的O
        # 然后遍历整个board，如果碰到了标记过的内容，即不能被包围的O，就把他变回O
        # 如果碰到了O，这是可以被包围的O，没有被打上标记，因此要变成X
        
        n = len(board)
        m = len(board[0])
        
        if n == 0:
            return [[]]
        
        
        def dfs(x, y):
            # 我们是从边界的O为入口进入这个dfs，因此要先标记这是可以从边界走到的O
            board[x][y] = '#'
            
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                
                # 如果从边界出发走到的点在网格内，且是O，我们就dfs这个点，再把它标记起来为边界可以走到的点
                if 0 <= a < n and 0 <= b < m and board[a][b] == 'O':
                    dfs(a, b)
            
        for i in range(n):
            if board[i][0] == 'O': # 如果左边那一列是O
                dfs(i, 0)
            if board[i][m - 1] == 'O': # 如果右边那一列是O
                dfs(i, m - 1) 
        
        for j in range(m):
            if board[0][j] == 'O': # 如果上面那一行是O
                dfs(0, j)
            if board[n - 1][j] == 'O': # 如果下面那一行是O
                dfs(n - 1, j)
    
        # 至此，所有从边界可以走到的O，即未被包围的O，已经被标记成#，接下来我们只要遍历整个网格恢复return的形式即可
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
        return board
            