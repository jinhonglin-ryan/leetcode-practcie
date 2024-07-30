class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = 0
        next_gain = 0
        for num in gain:
            next_gain = next_gain + num
            res = max(res, next_gain)
        
        return res 