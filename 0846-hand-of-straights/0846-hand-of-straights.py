class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
    
        num_freq = defaultdict(int)
        
        for num in hand:
            num_freq[num] += 1
                
        
        for num in sorted(num_freq.keys()):
            # 从小到大遍历 hand中的非重复数字，每次取最小的最为起点，那么如果最小数有freq次出现，则理应有freq个以这个最小数开头的subgroup, 如果没有的话，就不成立，return False
            freq = num_freq[num]
            
            if freq == 0:
                continue
            
            
            for i in range(groupSize):
                num_freq[num + i] -= freq
                if num_freq[num + i] < 0:
                    return False
                
        return True
                
        
        
            
            