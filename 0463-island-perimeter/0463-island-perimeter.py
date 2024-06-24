class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
#         # Method 1: 定义dfs函数，计算岛屿的周长
#         def dfs(x, y):
#             # 检查当前坐标是否在网格范围内，如果不在则返回1，表示这是边界的一部分
#             if not 0 <= x < len(grid) or not 0 <= y < len(grid[x]):
#                 return 1
            
#             # 如果当前位置是水（即为0），也返回1，表示这是边界的一部分
#             if grid[x][y] == 0:
#                 return 1
            
#             # 如果当前位置已经访问过（即为2），返回0，不计入周长
#             if grid[x][y] == 2:
#                 return 0 
            
#             # 将当前陆地标记为已访问
#             grid[x][y] = 2
            
#             # 递归调用dfs函数计算上下左右四个方向的周长
#             return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
        
#         # 遍历网格的每个位置
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 # 如果当前坐标是陆地（即为1），开始计算周长
#                 if grid[i][j] == 1:
#                     return dfs(i, j)
                
#         # 如果网格中没有陆地，返回0
#         return 0
        
        # Method 2:直接遍历
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: # 题目中说只有一个陆地
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if not 0 <= x < len(grid) or not 0 <= y < len(grid[i]):
                            res += 1
                        elif grid[x][y] != 1:
                            res += 1
        return res 