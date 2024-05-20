class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_len = 0
        left = 0
        right = 0
        
        window = Counter(s)
        curr_window = Counter()
        
        while right < len(s):
            curr_window[s[right]] += 1
            
            while right - left + 1 > max(curr_window.values()) + k:
                curr_window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len 
            