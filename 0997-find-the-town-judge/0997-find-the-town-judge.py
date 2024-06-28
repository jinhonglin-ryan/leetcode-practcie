class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust == [] and n == 1:
            return 1
        elif trust == [] and n != 1:
            return -1 
        
        
        graph = defaultdict(list)
        inDegrees = [0 for _ in range(n + 1)]
        
        for e in trust:
            a = e[0]
            b = e[1]
            graph[a].append(b)
            inDegrees[b] += 1
            
        max_i = -1
        max_indegrees = 0
        
        for i in range(1, n + 1):
            if inDegrees[i] > max_indegrees:
                max_indegrees = inDegrees[i]
                max_i = i
                
        if inDegrees[max_i] == n - 1 and graph[max_i] == []:
            return max_i 
        else:
            return -1 
                            