class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        # 主要思想：假如车B在车A的后面，而车B到终点线的时间小于等于车A，那么就知道车A和B一定会组成车队一起过线。
        # 这样的话，就可以从离终点最近的一辆车开始，先算出其撞线的时间，然后再一次遍历身后的车，若后面的车撞线的时间小于等于前面的车的时间，则会组成车队。反之，若大于前面的车的时间，则说明无法追上前面的车，于是自己会形成一个新的车队，且是车头
        
        n = len(position)
        id = [i for i in range(n)]
        # 根据position排序，从position小排序到position大
        # 因此 id[0] 表示position最小的index（离target最远的index）
        # id[n - 1] 表示position最大的index（离target最近的index）
        id.sort(key=lambda x: position[x])
        
        
        # 假设res = n，也就是n辆车都成fleet到达destination，然后我们更新这个res
        res = n
        last = 0.0
        # 从离终点最近的车开始
        for i in range(n - 1, -1, -1):
            t = (target - position[id[i]]) / float(speed[id[i]])
            # 如果当前车到达终点的时间小于前一辆车（前一辆车指离终点更近的那辆车）
            # 那么这两个车会形成一个fleet, res -= 1
            if t <= last:
                res -= 1
            else:
            # 如果当前车到达终点的时间大于前一辆车，那么不会形成车队
            # 且 当前车可能是一个车队的头，last = t
                last = t
        
        return res
        