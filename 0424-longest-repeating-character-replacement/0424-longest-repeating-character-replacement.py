class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        """
        滑动窗口
        * 核心思想：
        1.
            如果当前窗口的间距 > 当前出现最大次数的字符的次数 + k 时
            意味着替换 k 次仍不能使当前窗口中的字符全变为相同字符，
            则此时应该将左边界右移，同时将原先左边界的字符频次减少。
        2.  
            可以考虑 s=DBCAB, k=2, 最好应该是BBBB, output为4
            go through code to see how max len is updated
        """
        
        max_len = 0
        left = 0
        right = 0
        
        window = Counter(s)
        curr_window = Counter()
        
        while right < len(s):
            # update当前right指针指向的character的frequency
            curr_window[s[right]] += 1
            
            # 当当前窗口间距 > 当前出现最大次数的字符的次数 + k
            # 替换 k 次不能使当前窗口中的字符全变为相同字符
            while right - left + 1 > max(curr_window.values()) + k:
                curr_window[s[left]] -= 1
                left += 1
                
            # 当当前窗口间距 <= 当前出现最大次数的字符的次数 + k时
            # 替换 k 次可以使得当前窗口中的字符全变为相同字符
            # 所以在这维护max_len
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len 
            