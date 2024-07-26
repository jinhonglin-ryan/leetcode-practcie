class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        res = [False for _ in range(len(candies))]
        
        for i in range(len(candies)):
            now = candies[i]
            max_kid = max(candies)
            after = now + extraCandies
            
            if after >= max_kid:
                res[i] = True
        return res 