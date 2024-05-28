class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # 创建一个最小堆，存储每个点及其距离的平方
        min_heap = []
        for index, (x, y) in enumerate(points):
            distance_squared = x**2 + y**2
            heapq.heappush(min_heap, (distance_squared, index))
        
        # 从堆中获取最小的k个距离，将对应的点放入结果列表
        result = []
        while k > 0 and min_heap:
            _, index = heapq.heappop(min_heap)
            result.append(points[index])
            k -= 1
        
        return result
        