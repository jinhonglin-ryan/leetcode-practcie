class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        定义DFS函数 (dfs 方法)：

        dfs(x, y) 函数接收一个网格坐标 (x, y) 并计算从该位置开始的岛屿周长。
        如果当前坐标不在网格范围内，返回1，表示这是边界的一部分。
        如果当前坐标是水（即 grid[x][y] == 0），返回1，表示这是边界的一部分。
        如果当前坐标已经访问过（即 grid[x][y] == 2），返回0，不计入周长。
        如果当前坐标是陆地（即 grid[x][y] == 1），将其标记为已访问（即 grid[x][y] = 2）。
        递归调用 dfs 函数，计算该坐标的上下左右四个方向的周长，并将结果相加。
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
        # 定义四个方向的移动（上、右、下、左）
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        # 初始化周长结果为0
        res = 0
        
        # 遍历网格的每个位置
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 如果当前位置是陆地（即为1）
                if grid[i][j] == 1:
                    # 遍历四个方向
                    for k in range(4):
                        # 计算新位置的坐标
                        x = i + dx[k]
                        y = j + dy[k]
                        
                        # 检查新位置是否在网格范围内
                        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[i])):
                            # 如果新位置在网格外，说明这是边界的一部分，周长加1
                            res += 1
                        elif grid[x][y] != 1:
                            # 如果新位置不是陆地（即不是1），说明这是边界的一部分，周长加1
                            res += 1
        
        # 返回计算出的周长结果
        return res