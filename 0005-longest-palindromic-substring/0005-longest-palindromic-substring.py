class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Method 1: DP
        # dp[i][j] 表示s在[i:j+1]中是不是一个palindrome
        
        n = len(s)
        
        if n == 0:
            return ''
        
        if n == 1:
            return s
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # 对于单个字符而言，其肯定是回文串，因此初始化dp为如下
        for i in range(n):
            dp[i][i] = True
            
        max_len = 1
        max_len_start = 0
        
        # 区间DP的写法：外层枚举长度，内层枚举左端点
        for length in range(1, n + 1): # 子串长度从 1 到 n
            for i in range(n - length + 1): # 枚举左端点位置
                # j - i + 1 = length
                j = length + i - 1 # 子串结束位置
                
                # 如果当前的两个端点相同
                if s[i] == s[j]:
                    # 如果字符串的大小（包含i和j的两个端点）为1，2，或者3
                    # 那么该字符串肯定是回文串
                    # 比如a, aa, aba, 分别对应i和j指向同一个字符，i和j中间没有隔任何字符，i和j中间只隔了一个字符，这都是回文串
                    if length <= 3:
                        dp[i][j] = True
                    else: # 处理更长的字符串的情况
                        dp[i][j] = dp[i + 1][j - 1] # 我们外层循环按照长度枚举可以确保这里的依赖关系是成立的 dp[i][j] = dp[i + 1][j - 1] 即 dp[i + 1][j - 1]是在前面外层循环计算过的（即更短的长度的时候的循环）
                        
                # 如果当前是回文串，且长度大于最大的，更新
                if dp[i][j] and length > max_len:
                    max_len = length
                    max_len_start = i
        return s[max_len_start: max_len_start + max_len]
    
                        
        
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

        