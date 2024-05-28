class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # 思路：把nums搞成大顶堆
        # heapq 模块默认只提供了最小堆的实现
        # 技巧：在添加元素到堆之前，将每个元素取反，然后用heapq.heappush将元素加入堆中
        # 取出堆顶元素后，再取反，来获得起始元素
        max_heap = []
        for stone in stones:
            stone = -stone
            heapq.heappush(max_heap, stone)
        
        while len(max_heap) > 1:  # 只要堆中元素多于一个，就继续处理
            stone1 = -heapq.heappop(max_heap)  # 取出最大石头，同时取反恢复原值
            stone2 = -heapq.heappop(max_heap)  # 取出第二大石头，同样取反恢复原值
            if stone1 != stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))  # 如果不相等，把差值取反后推回堆中

        return -max_heap[0] if max_heap else 0  # 如果堆非空，返回堆顶元素的相反数，否则返回 0