class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        # 贪心思路：枚举起点
        # 每个起点，都看一下油箱剩余的油量 + 当前起点补充的油量 能不能 > 走到下一个站的消耗
        # 如果我们起点在i，然后枚举到j的时候发现 不能走到j+1个站，也就说明我们从i出发最多只能走到第j个站
        # 在j的时候 left + gas[j] 是 < cost[j]的
        # 因此我们更新起点为j+1，且不考虑i到j中的任何点作为我们的起点，因为
        # 比如我们最多只能从i走到j，i到j中有一个站k，k不可能最为我们的起点，因为我们在从i-j的时候必然经过k，
        # 且经过k的时候left 是 > 0的，有一定累加油量之后也最多只能走到j，那么如果k作为起始位置，没有油，必然不会超过j
        # 因此下一个起点直接为 j + 1 
        
        n = len(gas)
        i = 0
        
        while i < n: # 枚举起点
            remaining = 0
            j = 0
            while j < n: # 枚举从当前i开始走，最多走多长，环形下标
                k = (i + j) % n
                remaining += gas[k] - cost[k]
                
                if remaining < 0:
                    break
                j += 1
                
            # 如果循环是由j走了n步之后退出的，而不是油量<0，说明i可以作为起点   
            if j == n:
                return i
            
            i = i + j + 1
        
        return -1
                
            
            