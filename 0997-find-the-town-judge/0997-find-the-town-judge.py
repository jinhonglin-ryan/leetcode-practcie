class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        # 法官存在：该法官出度为0，入度为n-1
        outDegrees = [0 for _ in range(n + 1)]
        inDegrees = [0 for _ in range(n + 1)]
        
        for e in trust:
            a = e[0]
            b = e[1]
            outDegrees[a] += 1
            inDegrees[b] += 1
            
        res = -1
        
        for i in range(1, n + 1):
            if outDegrees[i] == 0 and inDegrees[i] == n - 1:
                if res != -1: # 如果已经有多个法官，则不合法，return -1
                    return -1
                res = i
                
        return res
                            