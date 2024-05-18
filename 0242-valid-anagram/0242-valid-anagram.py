class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Method 1: use sorted()
        # if two strings after sorted are equal, they are anagrams
        # if sorted(s) == sorted(t):
        #     return True
        # return False
    
        
        # Method 2: use Dictionary to store count of each character
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}
        
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        return s_count == t_count