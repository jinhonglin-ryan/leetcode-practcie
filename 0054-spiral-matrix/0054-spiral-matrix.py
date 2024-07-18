class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1 
        
        
        while True:
            # 先遍历第一行
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
                
            # 再遍历最右边竖着的
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
                
            # 再遍历最下面
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up:
                break
                
            # 再遍历最左边竖着的
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
                
        return res 
    
                
                
            