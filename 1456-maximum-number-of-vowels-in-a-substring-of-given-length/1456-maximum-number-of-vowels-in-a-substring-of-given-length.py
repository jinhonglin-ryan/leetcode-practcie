class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Method 1. 
        left, right = 0, 0
        ans = 0
        window_count = 0
        vowel_set = ('a','e','i','o','u')

        while right < len(s):
            if s[right] in vowel_set:
                window_count += 1

            if right - left + 1 >= k:
                ans = max(ans, window_count)
                if s[left] in vowel_set:
                    window_count -= 1
                left += 1

            right += 1
        return ans

        
#         # Method 2. 
#         vowels = set(['a', 'e', 'i', 'o', 'u'])
#         max_cnt = -1
        
#         left, right = 0, 0
        
#         curr_sub = ""
#         curr_cnt = 0
        
#         while right < k:
#             curr_sub += s[right]
#             right += 1
            
#         for ch in curr_sub:
#             if ch in vowels:
#                 curr_cnt += 1
        
#         max_cnt = max(max_cnt, curr_cnt)
        
#         while right < len(s):
#             first = curr_sub[0]
#             if first in vowels:
#                 curr_cnt -= 1
            
#             curr_sub = curr_sub[1:]
#             now = s[right]
#             curr_sub += now
#             right += 1
            
#             if now in vowels:
#                 curr_cnt += 1
                
#             max_cnt = max(max_cnt, curr_cnt)  
            
#         return max_cnt
            
            
            
        
        
        