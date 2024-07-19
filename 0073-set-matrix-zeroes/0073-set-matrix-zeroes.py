class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        todo = []
        
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    todo.append([i, j])
            
        todo = deque(todo)
        while todo:
            a, b = todo.popleft()
            
            for j in range(m):
                if matrix[a][j] != 0:
                    matrix[a][j] = 0
                    
            for i in range(n):
                if matrix[i][b] != 0:
                    matrix[i][b] = 0
                    
        
            
            