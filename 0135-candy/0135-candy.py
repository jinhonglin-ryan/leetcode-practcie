class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        # 初始每个小孩有一个糖果 
        # 要考虑一个小孩两边的情况，我们用两个遍历来完成
        # 1. 从前往后遍历，考虑如果当前小孩的得分高于前一个小孩，糖果就多一个
        # 2. 从后往前遍历，如果当前小孩的得分高于后一个小孩，糖果就多一个，并且与1的情况取max值
        
        n = len(ratings)
        candies = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        return sum(candies)
                                    
                                    