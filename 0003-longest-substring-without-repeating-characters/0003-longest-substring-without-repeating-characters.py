class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0 
        right = 0 
        substr_count = {}
        max_len = 0
        
        while right < len(s):
            if s[right] not in substr_count:
                substr_count[s[right]] = 1
            else:
                substr_count[s[right]] += 1
                
                while substr_count[s[right]] > 1:
                    substr_count[s[left]] -= 1
                    left += 1
            
            
                
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len 
            
                
                    
                
    