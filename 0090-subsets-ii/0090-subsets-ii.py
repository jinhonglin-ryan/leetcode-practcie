class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        used = [False for _ in nums]
        nums = sorted(nums)
        
        def backtrack(nums, path, used, startIndex):
            ans.append(path[:])
            if startIndex >= len(nums): 
                return
            
            for i in range(startIndex, len(nums)):
                if (i > 0) and (nums[i - 1] == nums[i]) and (used[i - 1] == False):
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, path, used, i + 1)
                used[i] = False
                path.pop()
                
        backtrack(nums, path, used, 0)
        return ans 
        