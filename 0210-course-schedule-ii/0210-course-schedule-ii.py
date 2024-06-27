class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        edges = prerequisites
        n = numCourses
        
        g = defaultdict(list)
        
        # 下标为课程，获得的数值为这个课程的入度
        inDegrees = [0 for _ in range(n)]
        
        # 或者可以写 g = dict()
        # for i in range(n):
        #     g[i] = []
        
        for e in edges:
            a = e[0]
            b = e[1]
            g[b].append(a)
            inDegrees[a] += 1
        
        queue = deque()
        
        # 对于所有课程，把入度为0的加入queue
        for i in range(n):
            if inDegrees[i] == 0:
                queue.append(i)
        
        count = 0
        ans = []
        while queue:
            t = queue.popleft()
            count += 1
            ans.append(t)
            for v in g[t]:
                inDegrees[v] -= 1
                if inDegrees[v] == 0:
                    queue.append(v)
        
        if count != numCourses:
            return []
        return ans 
        
        
            