class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        l, r = 0, len(s) - 1
        s = list(s)
        
        while l < r:
            left = s[l]
            right = s[r]
            
            if left in vowels and right in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif left in vowels:
                r -= 1
            elif right in vowels:
                l += 1
            else:
                l += 1
                r -= 1
                
        return "".join(s)