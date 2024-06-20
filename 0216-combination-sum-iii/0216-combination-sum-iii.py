class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        
        def backtrack(startIndex, path):
            if sum(path) > n:
                return
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path[:])
                
            for i in range(startIndex, 10):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
    
        
        backtrack(1, path)
            
        return ans