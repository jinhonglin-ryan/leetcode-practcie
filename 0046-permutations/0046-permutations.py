class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        used = [False for _ in nums]
        
        def backtrack(nums, path):
            if len(path) == len(nums):
                ans.append(path[:])
                
            for i in range(0, len(nums)):
                if used[i] == True:
                    continue
                else:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, path)
                    used[i] = False
                    path.pop()
        backtrack(nums, path)
        return ans 
                