class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        滑动窗口
        用"substr_count"这个dictionary记录每个char出现的次数
        left和right都一开始指向0
        移动right(窗口的right指针，直到s末尾)
        
        """
        
        left = 0 
        right = 0 
        substr_count = {}
        max_len = 0
        
        while right < len(s):
            # 如果当前right指向的char不在substr_count中，我们把该char加入substr_count且occurrence设成1
            if s[right] not in substr_count:
                substr_count[s[right]] = 1
            else:
            # 如果当前right指向的char在substr_count中，其occurrence++
                substr_count[s[right]] += 1
            
            # 固定下这个right后，只要这个right char出现的occurrence还大于1，我们就一直移动left
            while substr_count[s[right]] > 1:
                # 每次移动left前，需要将现在left指向的char的occurrence —= 1
                substr_count[s[left]] -= 1
                # 移动left指针
                left += 1
                
            # 维护最大substring长度
            max_len = max(max_len, right - left + 1)
            
            # 再次尝试移动right指针，加入新的char into substr_count
            right += 1
        return max_len 
            
                
                    
                
    