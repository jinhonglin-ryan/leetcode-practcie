class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0 
        right = 0
        s_window = Counter(s)
        curr_window = Counter()
        max_len = 0
        
        
        while right < len(s):
            curr_window[s[right]] += 1
            
            while curr_window[s[right]] > 1:
                curr_window[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)    
            right += 1
        return max_len 