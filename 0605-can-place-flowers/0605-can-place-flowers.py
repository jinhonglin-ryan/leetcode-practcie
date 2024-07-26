class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        k = len(flowerbed)
        cnt = 0
        for i in range(k):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == k - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    cnt += 1
        return n <= cnt