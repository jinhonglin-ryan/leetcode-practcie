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
            
            for i in range(startIndex, len(nums)): # 我们要避免1，2 和 2，1的重复，所以要从startIndex之后去找
                path.append(nums[i])
                backtrack(nums, path, target, i) # 因为这里说一个数字可以用无数次，所以下一步还是可以从这个数字里找
                path.pop()
        
        backtrack(candidates, path, target, 0)
        return ans 