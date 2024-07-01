class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
#         # DFS
#         graph = defaultdict(list)
#         visited = set()
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
            
#         def dfs(node):
#             if node == destination:
#                 return True
            
#             if node in visited:
#                 return False
            
#             visited.add(node)
            
#             for neighbor in graph[node]:
#                 if dfs(neighbor):
#                     return True
#             return False
        
#         return dfs(source)
    
        # BFS
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        queue = deque()
        queue.append(source)
        visited = set()
        
        while queue:
            node = queue.popleft()
            
            if node in visited:
                continue 
            
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False 
            
        
        
        