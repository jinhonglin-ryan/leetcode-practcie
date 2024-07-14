class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # stack 
        
        # 用left stack存左括号的index
        # 用stars stack存星号的index
        # 遇到)后，先弹出左括号，如果没有，则尝试弹出stars, 如果也没有，return false
        # 遍历结束后，left 和 stars 可能还有剩余，要检查stars可不可以用做) 跟 left匹配
        # 可以匹配的条件是，stars的index必须大于left的index
        # 如果left最后为空，则满足条件，剩下的stars可以作为空字符串
        
        left = list()
        stars = list()
        
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
                continue 
            elif s[i] == '*':
                stars.append(i)
                continue
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
                
        # 检查未匹配的 '(' 是否能被 '*' 匹配
        while left and stars:
            if left[-1] < stars[-1]:
                left.pop()
                stars.pop()
            else:
                return False
            
        return len(left) == 0
                
                