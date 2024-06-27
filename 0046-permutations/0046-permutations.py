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
                
            for i in range(0, len(nums)): # 对于permutation，重复的比如12和21是都要考虑的。所以每次都从整个nums里面找没有使用过的数字
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