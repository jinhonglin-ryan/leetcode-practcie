class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        used = [False for _ in nums] # 为了进行去重 需要知道哪些数被用过
        nums = sorted(nums) # 要进行去重的话，要在树层上去重，需要将nums排序
        
        def backtrack(path, startIndex):
            ans.append(path[:])
            
            if startIndex >= len(nums): 
                return
            
            # startIndex 用于保证每一个数只用一次
            for i in range(startIndex, len(nums)):
                # 如果当前的number 跟前一个number是一样的，并且前一个number没被用，是树层上的重复，需要去重
                if (i > 0) and (nums[i - 1] == nums[i]) and (used[i - 1] == False): # 对树枝不去重，对树层上的去重
                    continue
                    
                path.append(nums[i])
                used[i] = True
                backtrack(path, i + 1) # 在subset问题的时候，为了避免重复，我们要从当前位置之后开始找，也就是i+1
                used[i] = False
                path.pop()
                
        backtrack(path, 0)
        return ans 
        