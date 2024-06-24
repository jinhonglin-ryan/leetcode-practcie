class Solution(object):
    def __init__(self):
        self.g = None  # 用于存储输入的网格
        self.count = 0  # 用于计数岛屿数量
        
    def dfs(self, x, y):
        # 定义四个可能的移动方向
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        # 将当前节点标记为已访问
        self.g[x][y] = 0
        
        # 遍历四个方向
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            # 检查新位置是否在网格范围内且是否是陆地('1')
            if (a >= 0 and a < len(self.g) and b >= 0 and b < len(self.g[a]) and self.g[a][b] == '1'):
                # 递归调用 dfs 进行深度优先搜索
                self.dfs(a, b)
                
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # flood fill算法，通过 DFS 实现
        self.g = grid  # 将输入的网格赋值给实例变量
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                # 如果当前节点是陆地('1')
                if self.g[i][j] == '1':
                    # 进行DFS，将连接的所有陆地标记为已访问
                    self.dfs(i, j)
                    # 每找到一个新的岛屿，岛屿计数器加1
                    self.count += 1
        # 返回总的岛屿数量
        return self.count
