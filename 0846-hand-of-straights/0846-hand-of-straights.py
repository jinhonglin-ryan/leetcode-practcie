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
            freq = num_freq[num]
            
            if freq == 0:
                continue
            
            
            for i in range(groupSize):
                num_freq[num + i] -= freq
                if num_freq[num + i] < 0:
                    return False
                
        return True
            
            
                
        
                
        
        
            
            