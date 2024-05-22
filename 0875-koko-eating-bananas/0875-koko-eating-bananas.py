class Solution(object):
    
    
    # 比如k是eating speed, 要求k的最小值在这个表达式里:
    # summation of ceil(pile[i] / k) <= h
    # 选ceiling因为如果我们需要4.5小时才能吃完一个pile, 在这题的语境下就是5小时
    # ceiling的算法技巧：a/b的ceiling = (a+b-1)/b 的floor
    
    def check_if_can_eat(self, piles, hour, speed):
        time = 0
        # 计算在当前speed下可否在h小时内吃完
        for pile in piles:
            time += (pile + speed - 1) // speed 
            
        return time <= hour
    
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not self.check_if_can_eat(piles, h, mid):
                left = mid + 1
            else:
                right = mid

        return right