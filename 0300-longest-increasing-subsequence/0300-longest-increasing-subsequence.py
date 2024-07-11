class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP问题
        # dp[i] 表示为：以nums[i] 结尾的最长递增子序列长度。
        # 返回答案为 dp数组中最大的值
        # 初始化dp所有entry为1，即自己本身


        n = len(nums)
        # 初始时每个位置的最长子序列至少包括自己，所以初始值为 1。
        dp = [1 for _ in range(n)]
        
        # 一般遍历，外层遍历终点，内层遍历起点
        for i in range(1, n):
            for j in range(i):
                # 如果nums[i] > nums[j]，意味着 nums[i] 可以接在以 nums[j] 结尾的子序列之后形成一个新的更长的子序列
                if nums[i] > nums[j]:
                    # dp[j] 是以 nums[j] 结尾的最长严格递增子序列的长度，加上 nums[i] 之后，这个长度就变成 dp[j] + 1。
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # dp[i] 只表示以 nums[i] 结尾的子序列长度，不代表整个数组的最长子序列。整个数组的最长递增子序列可能出现在任何位置，因此需要遍历整个 dp 数组找到最大值，才能得到整个数组的最长递增子序列长度。
        return max(dp)
        
        
            