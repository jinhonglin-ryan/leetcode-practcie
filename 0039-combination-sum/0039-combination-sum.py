class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backtrack(nums, path, target, startIndex):
            if sum(path) == target:
                ans.append(path[:])
            if sum(path) > target:
                return
            
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, target, i)
                path.pop()
        
        backtrack(candidates, path, target, 0)
        return ans 