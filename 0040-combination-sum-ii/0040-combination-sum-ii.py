class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        used = [False for _ in candidates] # 为了进行去重 需要知道哪些数被用过
        candidates = sorted(candidates) # 要进行去重的话，要在树层上去重，需要将candidates排序
        
        # startIndex 用于保证每一个数只用一次
        def backtrack(candidates, target, path, startIndex):
            if sum(path) == target:
                ans.append(path[:])
            if sum(path) > target:
                return
            
            for i in range(startIndex, len(candidates)):
                # 树层上的去重处理 树枝上不去重
                # 如果当前的number 跟前一个number是一样的，并且前一个number没被用，是树层上的重复，需要去重
                if i > 0 and candidates[i - 1] == candidates[i] and used[i - 1] == False:
                    continue
                path.append(candidates[i])
                used[i] = True
                backtrack(candidates, target, path, i + 1)
                used[i] = False
                path.pop()
                
        backtrack(candidates, target, path, 0)
        return ans 