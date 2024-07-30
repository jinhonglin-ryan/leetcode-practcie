class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        
        for x in asteroids:
            if x > 0:
                stack.append(x)
                
            else:
                # 如果stack内有东西，且当前的x是向左移动，stack的top是向右移动，会发生碰撞
                while stack and x < 0 < stack[-1]:
                    # 如果当前的x跟stack top的质量一样，两个都爆炸，移出top，直接进入下一个asteroids的iteration
                    if abs(stack[-1]) == abs(x):
                        stack.pop()
                        break

                    # 如果x在碰撞后保留，移出stack的top，继续检验while
                    elif abs(stack[-1]) < abs(x):
                        stack.pop()
                    
                    # 当前x在碰撞中没了
                    else:
                        break 
                        
                else: 
                    stack.append(x)
                    
        return stack 
                
            
                    
            
            
            
        