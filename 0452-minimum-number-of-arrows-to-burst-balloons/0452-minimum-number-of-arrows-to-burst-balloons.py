class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if not points:
            return 0
        
        # 按照气球的右边界进行排序
        points.sort(key=lambda x: x[1])
        
        count = 1  # 至少需要一支箭
        end = points[0][1]  # 第一支箭的位置
        
        for x, y in points:
            # 如果当前气球的左边界在箭的位置右边，需要一支新的箭
            if x > end:
                count += 1
                end = y  # 更新箭的位置为当前气球的右边界
        
        return count
                    
             
        