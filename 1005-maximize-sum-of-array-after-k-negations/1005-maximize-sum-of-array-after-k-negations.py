class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 贪心
        # 先按照绝对值将nums排序
        # 遍历排序后的数组，碰到的负数都取反，消耗k
        # 遍历结束后，看k，如果k还有，说明我们数组里已经全是正数了，且是奇数，那就对数组里最小的那个数取反1次即可
        # 如果k是偶数，不管，因为最小的正数偶数次取反后还是原先的值
        
        nums.sort(key=lambda x: abs(x), reverse = True)
        
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
                
        if k % 2 == 1:
            nums[len(nums) - 1] *= -1
            
        return sum(nums)
        