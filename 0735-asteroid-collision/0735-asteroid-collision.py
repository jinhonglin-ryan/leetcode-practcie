class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        
        for x in asteroids:
            if not stack or x > 0:
                stack.append(x)
                
            
            else:                
                while stack and 0 < stack[-1] < -x:
                    stack.pop()
                    
                if not stack or stack[-1] < 0:
                    stack.append(x)
                    
                elif stack[-1] == -x:
                    stack.pop()
                    
        return stack 
            
                
            
                    
            
            
            
        