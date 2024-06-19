class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(start, path):
        # 添加当前子集到结果中
            res.append(path[:])  # 使用path[:]来避免引用问题
            # 从start开始，尝试包含更多的元素
            for i in range(start, len(nums)):
                # 添加当前元素到路径
                path.append(nums[i])
                # 递归，移动到下一个元素
                backtrack(i + 1, path)
                # 回溯，移除路径中的最后一个元素
                path.pop()
    
        res = []
        backtrack(0, [])
        return res