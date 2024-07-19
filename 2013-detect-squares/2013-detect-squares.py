class DetectSquares(object):

    def __init__(self):
        # 存所有点的frequency
        self.points_count = defaultdict(lambda: defaultdict(int))
        
        # 存每个 x 坐标对应的所有 y 坐标集合
        self.rows = defaultdict(set)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.points_count[x][y] += 1
        self.rows[x].add(y) 
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        total_squares = 0
        
        for v in self.rows[x]:
            if v == y:
                continue  # 跳过相同的点

            # 以 y 到 v 的距离作为正方形的边长 len
            side_length = abs(y - v)

            # 计算以当前点作为正方形一顶点，是否存在其余三个顶点
            total_squares += (
                self.points_count[x][v] * 
                self.points_count[x + side_length][y] * 
                self.points_count[x + side_length][v]
            )
            total_squares += (
                self.points_count[x][v] * 
                self.points_count[x - side_length][y] * 
                self.points_count[x - side_length][v]
            )

        return total_squares
        
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)