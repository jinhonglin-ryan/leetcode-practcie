class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        count = -1
        
        end = intervals[0][1]
        
        for a, b in intervals: 
            if a >= end: # 区间未重叠情况
                end = b
                continue
            else: # 两个区间重叠，需要更新边界为最小值
                count += 1
                end = min(end, b)
                
        return count 