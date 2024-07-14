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
        # 题目说了 triplets中都是>=1的正整数
        newa, newb, newc = 0, 0, 0
        
        # max操作无顺序要求
        for a, b, c in triplets:
            # 如果当前triplet内都是小于target的值，可以做max的操作
            # 否则max会超过target，得不到结果
            if a <= x and b <= y and c <= z:
                newa = max(a, newa)
                newb = max(b, newb)
                newc = max(c, newc)
                
        return (newa, newb, newc) == (x, y, z)