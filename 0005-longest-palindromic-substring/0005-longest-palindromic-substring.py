class Solution(object):
    def check_palindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        max_len = 0
        longest_pal = s[0]  # 初始化为第一个字符，保证至少有一个字符返回

        for i in range(len(s)):
            # Explore palindromes of odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    longest_pal = s[l:r+1]
                l -= 1
                r += 1

            # Explore palindromes of even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    longest_pal = s[l:r+1]
                l -= 1
                r += 1

        return longest_pal

        