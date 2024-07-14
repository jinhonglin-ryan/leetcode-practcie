class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        # 记录下每个字符的最远出现下标
        num_last_index = {}
        
        for i in range(len(s)):
            num_last_index[s[i]] = i
        
        
        start = 0
        end = 0
        res = []
        
        for i in range(len(s)):
            end = max(end, num_last_index[s[i]])
            
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res 
            
            
        
            
        