class Solution(object):
    
    
    # 比如k是eating speed, 要求k的最小值在这个表达式里:
    # summation of ceil(pile[i] / k) <= h
    # 选ceiling因为如果我们需要4.5小时才能吃完一个pile, 在这题的语境下就是5小时
    # ceiling的算法技巧：a/b的ceiling = (a+b-1)/b 的floor
    
    def check_if_can_eat(self, piles, hour, speed):
        # 检查是否可以在 mid(speed) 速度下在 h 小时内吃完所有香蕉：
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
        
        # left 和 right是eating speed 我们在这个范围内找最小的eating speed
        # left是1是因为eating speed是integer，最小的eating speed就只能是1
        # right是max(piles)是最大的那一堆里面的香蕉数量，因为我们如果eating speed 大于这个最大值，我们在一个小时吃完后也不会去吃别的，所以eating speed in that case is larger than necessary
        left = 1 
        right = max(piles)
        
        
        # 在这个left - right speed range里面找最小值 
        while left < right:
            # 计算中间速度, 检查是否可以在 mid 速度下在 h 小时内吃完所有香蕉：
            mid = left + (right - left) // 2
            if not self.check_if_can_eat(piles, h, mid):
                # 如果can eat function 返回False，说明速度 mid 太慢，无法在 h 小时内吃完所有香蕉，需要增加速度。因此，将 left 更新为 mid + 1。
                left = mid + 1
            else:
                # 如果可以吃完，说明速度 mid 可以在 h 小时内吃完所有香蕉，甚至可能更慢的速度也可以。因此，将 right 更新为 mid
                right = mid
                
        # 当 left 等于 right 时，循环结束。此时，left 和 right 都指向了可以在 h 小时内吃完所有香蕉的最小速度。
        return left