class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Method 1: DP
        # dp[i][j] 表示s在[i:j+1]中是不是一个palindrone
        
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        max_len = 1
        max_start_pos = 0 
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if (j - 1) - (i + 1) <= 0:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_start_pos = i
        return s[max_start_pos:max_start_pos + max_len]         
                    
        
#         # Method 2: 
#         # 中心扩展法：这种方法对每一个可能的中心位置进行扩展，尝试找出最长的回文子串。
#         # 对于输入字符串中的每个字符，都尝试将其作为回文的中心，并向两边扩展。
#         # 分别检查以该字符为中心的奇数长度回文（如 "aba"）和偶数长度回文（如 "abba"）。
        
#         if not s:
#             return ""
        
#         max_len = 0
#         longest_pal = s[0]  # 初始化为第一个字符，保证至少有一个字符返回
        
#         # 使用两个指针 l（left）和 r（right），初始化为当前中心位置。
#         # 对于奇数长度，两个指针都从 i 开始；
#         # 对于偶数长度，l 从 i 开始，r 从 i + 1 开始。
#         for i in range(len(s)):
#             # Explore palindromes of odd length
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > max_len:
#                     max_len = r - l + 1
#                     longest_pal = s[l:r+1]
#                 l -= 1
#                 r += 1

#             # Explore palindromes of even length
#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > max_len:
#                     max_len = r - l + 1
#                     longest_pal = s[l:r+1]
#                 l -= 1
#                 r += 1

#         return longest_pal

        