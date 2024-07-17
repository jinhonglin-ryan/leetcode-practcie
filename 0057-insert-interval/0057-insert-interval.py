class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        x, y = newInterval
        
        # 分成三个部分，左边完全没交集的，有交集的，右边完全没交集的
        
        k = 0
        
        # 左边完全没交集的
        while k < len(intervals) and intervals[k][1] < x:
            res.append(intervals[k])
            k += 1
            
        # 如果整个区间都没有重叠，直接加入newInterval 返回即可 
        if k == len(intervals):
            res.append([x, y])
            return res
        
        # 如果重叠了, 且没有走到区间末尾，当前的intervals[k][1] >= x
        elif k < len(intervals):
            
            x = min(x, intervals[k][0])
            while k < len(intervals) and intervals[k][0] <= y:
                y = max(intervals[k][1], y)
                k += 1
                
        res.append([x, y])
        
        # 右半部分剩下重叠的区域 
        while k < len(intervals):
            res.append(intervals[k])
            k += 1
            
        return res 
            
            
            
        
        
            
                
        