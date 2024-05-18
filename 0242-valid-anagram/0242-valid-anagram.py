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
#         if len(s) != len(t):
#             return False
        
#         # dictionary: maps character to its count
#         s_count = {}
#         t_count = {}
        
#         # iterate over character
#         # dict.get(char, 0) means:
#         # 1. try to get the value that key "char" points to
#         # 2. if there is no such key "char" existed, return 0 
        
#         for char in s:
#             s_count[char] = s_count.get(char, 0) + 1
#         for char in t:
#             t_count[char] = t_count.get(char, 0) + 1
        
#         return s_count == t_count

        # Method 3: use Counter()
        return Counter(s) == Counter(t)