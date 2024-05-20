class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        """
        维护一个长度为字符串s1长度的固定长度的滑动窗口。
        """
        window_s1 = Counter(s1)
        window_s2 = Counter()
        window_size = len(s1)
        
        
        left = 0
        right = 0
        
        
        while right < len(s2):
            # 我们维护的window size使得window_s2 和 window_s1一定要same amount of elements，所以在loop的头部 check if window_s2 == window_s1，如果是，return True
            if window_s2 == window_s1:
                return True
            
            # 把right指向的当前character放入window_s2中
            window_s2[s2[right]] += 1
            
            # 因为我们每次对s2_window_size的修改+=1 所以当current s2 window size == expected window size + 1 的时候 我们需要缩小 s2 window size by moving left pointer to right by one unit，使得current s2_window_size == expected_window_size
            if right - left + 1 == window_size + 1:
                window_s2[s2[left]] -= 1
                if window_s2[s2[left]] == 0:
                    del window_s2[s2[left]]
                left += 1
            # 维护完window size后，把right指针向右移动，进入下一次iteration，见iteration的开头注释    
            right += 1
        
        # 保证edge case s1 == adc, s2 == dcda
        # 大while loop结束后要check window_s2 和 window_s1 是否一样
        # 大while loop 结束前刚把第一个d remove from window_s2这时loop结束
        # 因此需要check remove完之后window_s1 和 window_s2 是否一样 
        if window_s2 == window_s1:
            return True
        return False