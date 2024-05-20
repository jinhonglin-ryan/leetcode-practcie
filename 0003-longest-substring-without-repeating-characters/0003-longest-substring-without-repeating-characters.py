class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 0
        window = {}
        max_len = 0
        
        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else: 
                window[s[right]] += 1
        
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)   
            right += 1
        return max_len
                
                    
                
    