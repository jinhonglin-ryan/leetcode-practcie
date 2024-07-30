class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # stack中可能有+也可能有-
        stack = []
        
        for x in asteroids:
            if not stack or x > 0:
                stack.append(x)
                
            else:
                # 只要当前元素是向左移动，栈顶元素向右移动，且当前元素重量大于栈顶元素，栈顶元素被removed
                while stack and 0 < stack[-1] < -x:
                    stack.pop()
                    
                # 如果栈顶为空，或者栈顶元素也是向左移动的，不会碰撞，把当前元素加入栈
                if not stack or stack[-1] < 0:
                    stack.append(x)
                    
                # 如果栈顶元素正好跟当前元素的移动方向相反，且质量一样，栈顶元素也没了
                elif stack[-1] == -x:
                    stack.pop()
                    
        return stack 
            
                
            
                    
            
            
            
        