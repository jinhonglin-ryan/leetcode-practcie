class Solution(object):
    
    def can_eat(self, piles, speed, hours):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time <= hours
    
   
    
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if not self.can_eat(piles, mid, h):
                left = mid + 1 
            else:
                right = mid
                
        return left
         
        