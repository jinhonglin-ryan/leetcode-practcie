class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        used = [False for _ in candidates]
        candidates = sorted(candidates)
        
        def backtrack(candidates, target, path, startIndex):
            if sum(path) == target:
                ans.append(path[:])
            if sum(path) > target:
                return
            
            for i in range(startIndex, len(candidates)):
                if i > 0 and candidates[i - 1] == candidates[i] and used[i - 1] == False:
                    continue
                path.append(candidates[i])
                used[i] = True
                backtrack(candidates, target, path, i + 1)
                used[i] = False
                path.pop()
                
        backtrack(candidates, target, path, 0)
        return ans 