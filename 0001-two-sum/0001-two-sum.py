class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Method 1: 暴力解法
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
                
        # Method 2: 
        num_to_index = {}

    # 遍历数组
        for i, num in enumerate(nums):
            # 计算所需的补数
            complement = target - num

            # 检查补数是否已经在字典中
            if complement in num_to_index:
                # 如果在字典中，返回补数的索引和当前数字的索引
                return [num_to_index[complement], i]

            # 如果不在字典中，将当前数字和其索引加入字典
            num_to_index[num] = i

        # 如果没有找到符合条件的两个数字，返回一个空列表
        return []