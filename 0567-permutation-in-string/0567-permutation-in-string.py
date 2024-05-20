class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        
        window_s1 = Counter(s1)
        window_s2 = Counter()
        window_size = len(s1)
        
        
        left = 0
        right = 0
        
        while right < len(s2):
            if window_s2 == window_s1:
                return True
            
            window_s2[s2[right]] += 1
                   
            if right - left + 1 == window_size + 1:
                window_s2[s2[left]] -= 1
                if window_s2[s2[left]] == 0:
                    del window_s2[s2[left]]
                left += 1
                
            right += 1
        
        if window_s2 == window_s1:
            return True
        return False