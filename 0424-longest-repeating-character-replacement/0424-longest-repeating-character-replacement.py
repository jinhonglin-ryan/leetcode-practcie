class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_len = -1
        
        counter = Counter()
        right = 0
        left = 0
        
        while right < len(s):
            counter[s[right]] += 1
            
            while right - left + 1 > max(counter.values()) + k:
                counter[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
            
            right += 1
        
        return max_len
        