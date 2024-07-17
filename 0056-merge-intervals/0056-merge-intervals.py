class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        res = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > end: # 不重叠的情况
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
                
            else:  # 重叠的情况
                end = max(end, intervals[i][1])
                
        res.append([start, end])    
        return res
                
        