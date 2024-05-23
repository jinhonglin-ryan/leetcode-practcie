class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        id = list(range(n))
        id.sort(key=lambda x: position[x])
        
        res = n
        last = 0.0
        for i in range(n - 1, -1, -1):
            t = (target - position[id[i]]) / float(speed[id[i]])
            if t <= last:
                res -= 1
            else:
                last = t
        
        return res
        