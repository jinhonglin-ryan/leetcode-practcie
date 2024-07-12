class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        count = 0 
        g = sorted(g)
        s = sorted(s)
        
        g = deque(g)
        s = deque(s)
        
        while g and s:
            need = g[0]
            cookie = s.popleft()
            
            if cookie < need:
                continue
            
            else:
                g.popleft()
                count += 1
                
        return count