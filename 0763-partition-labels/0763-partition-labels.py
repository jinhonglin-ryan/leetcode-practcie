class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        # 记录下每个字符的最远出现下标
        num_last_index = {}
        
        for i in range(len(s)):
            # 一直覆盖，获得最远下标
            num_last_index[s[i]] = i
        
        
        start = 0
        end = 0
        res = []
        
        for i in range(len(s)):
            # 遍历s中的每个char，记录下当前区间的结束位置
            end = max(end, num_last_index[s[i]])
            
            # 如果走到结束位置了，就记录下当前区间的长度，并且下一个区间的起点从 i + 1开始
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res 
            
            
        
            
        