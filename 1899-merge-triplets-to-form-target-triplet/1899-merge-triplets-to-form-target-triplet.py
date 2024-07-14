class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # 0次max
        for triplet in triplets:
            if triplet == target:
                return True 
        
        x, y, z = target
        newa, newb, newc = 0, 0, 0
        
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                newa = max(a, newa)
                newb = max(b, newb)
                newc = max(c, newc)
                
        return (newa, newb, newc) == (x, y, z)