class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        nums = [i for i in range(n + 1)]
        
        res = [0 for _ in range(n + 1)]
        
        def getOne(a):
            count = 0
            while a > 0:
                if a & 1 == 1:
                    count += 1
                a >>= 1
            return count
        
        
        for i in range(len(nums)):
            cnt = getOne(nums[i])
            res[i] = cnt
            
        return res
            
            